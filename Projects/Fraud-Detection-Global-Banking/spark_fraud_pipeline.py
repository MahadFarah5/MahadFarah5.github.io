from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator, MulticlassClassificationEvaluator
import happybase
from datetime import datetime

spark = SparkSession.builder \
    .appName("FraudDetectionML_to_HBase") \
    .enableHiveSupport() \
    .getOrCreate()

df = spark.sql("""
SELECT
    CAST(V1 AS DOUBLE) AS V1,
    CAST(V2 AS DOUBLE) AS V2,
    CAST(V3 AS DOUBLE) AS V3,
    CAST(V4 AS DOUBLE) AS V4,
    CAST(V5 AS DOUBLE) AS V5,
    CAST(Amount AS DOUBLE) AS Amount,
    CAST(Time AS DOUBLE) AS Time,
    CAST(Class AS INT) AS label
FROM fraud_transactions
""").na.drop()

assembler = VectorAssembler(
    inputCols=["V1", "V2", "V3", "V4", "V5", "Amount", "Time"],
    outputCol="features",
    handleInvalid="skip"
)

featured_df = assembler.transform(df).select("features", "label")
train_df, test_df = featured_df.randomSplit([0.7, 0.3], seed=42)

rf = RandomForestClassifier(
    labelCol="label",
    featuresCol="features",
    numTrees=50,
    maxDepth=8,
    seed=42
)

model = rf.fit(train_df)
predictions = model.transform(test_df)

auc = BinaryClassificationEvaluator(
    labelCol="label",
    rawPredictionCol="rawPrediction",
    metricName="areaUnderROC"
).evaluate(predictions)

accuracy = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="accuracy"
).evaluate(predictions)

precision = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="weightedPrecision"
).evaluate(predictions)

recall = MulticlassClassificationEvaluator(
    labelCol="label",
    predictionCol="prediction",
    metricName="weightedRecall"
).evaluate(predictions)

print(f"AUC: {auc}")
print(f"Accuracy: {accuracy}")
print(f"Weighted Precision: {precision}")
print(f"Weighted Recall: {recall}")

run_id = "run_" + datetime.now().strftime("%Y%m%d_%H%M%S")
metrics = [
    (run_id, "cf:auc", str(auc)),
    (run_id, "cf:accuracy", str(accuracy)),
    (run_id, "cf:precision", str(precision)),
    (run_id, "cf:recall", str(recall))
]

def write_to_hbase_partition(partition):
    connection = happybase.Connection("master")
    connection.open()
    table = connection.table("fraud_metrics")
    for row_key, column, value in partition:
        table.put(row_key, {column: value.encode("utf-8")})
    connection.close()

spark.sparkContext.parallelize(metrics).foreachPartition(write_to_hbase_partition)
spark.stop()
