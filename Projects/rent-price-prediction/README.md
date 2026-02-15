# Rent Price Prediction

A predictive modeling project that estimates monthly rent prices based on property features and location. Combining data cleaning, feature engineering, regression, and machine learning for actionable insights.

# Project Overview

Monthly rent is a crucial financial decision for millions of renters worldwide, yet many factors that influence rental prices are poorly understood. In this project, I build an end-to-end data science workflow that:

- Cleans and preprocesses raw rental listing data  
- Engineers features that capture property characteristics  
- Trains and evaluates multiple predictive models  
- Interprets model results to understand key price drivers  

The goal is not just to predict rent but *explain what matters most* in a renter’s decision making process.

---

# Data Description

The dataset used in this project comes from Kaggle (House Rent Prediction Dataset). It includes approximately 4,700 rental listings with features such as:

| Feature | Description |
|---------|-------------|
| 'rent' | Monthly rent price (target) |
| 'size' | Area in square feet |
| 'bhk' | Number of bedrooms |
| 'bathroom' | Number of bathrooms |
| 'furnishing_status' | Furnished / semi-furnished / unfurnished |
| 'area_locality' | Neighborhood/area |
| 'city' | City |
| 'floor' | Floor info |
| 'tenant_preferred' | Tenant category |
| 'point_of_contact' | Contact type |

The dataset blends numerical and categorical variables, making it suitable for both traditional regression and advanced machine learning models.

---

# Key Questions Addressed

This project explores several core research questions, including:

1. Can rental price be accurately predicted from observable property features?
2. What features (e.g., size, bedrooms, location, furnishing status) drive rent the most?
3. Do complex models (e.g., tree-based methods) outperform simple regression?
4. How do predictions vary across cities and housing types?
5. What insights can renters and policymakers gain from the models?

---

# Methodology

The workflow follows a full data science pipeline:

 1. Data Cleaning
- Standardized column names
- Parsed and transformed the 'floor' field
- Handled missing values and corrected data types

# 2. Feature Engineering
- Created 'rent_per_sqft'
- Log-transformed rent to reduce skew
- Encoded categorical variables using one-hot encoding

# 3. Modeling
Baseline and advanced models were evaluated:

| Model | Purpose |
|-------|---------|
| Linear Regression | Baseline interpretability |
| Ridge / Lasso / Elastic Net | Regularized regression |
| Random Forest Regressor | Nonlinear relationships |
| Gradient Boosting (XGBoost) | High-performance prediction |

# 4. Evaluation
Models were compared using:
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² (coefficient of determination)
- Cross-validation performance

# 5. Interpretability
Feature importance was extracted using:
- Tree-based model importance
- SHAP values for model-agnostic explanations

---

# Illustrations & Visual Insights

The project includes several key visualizations:

- Distribution of rents (raw and log-scaled)
- Scatter plot: Rent vs. Size (with trend)
- Average rent by city (top 10)
- Average rent by furnishing status
- Rent per square foot by city

>  See the 'figures/' folder for all visuals.

---

# Repository Structure

