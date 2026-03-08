#DSC 510
#Week 2
#Programming Assignment Week 2
#Author Mahad Farah
#09/08/2024

#Change Control Log:
#Moved to Production: 09/08/2024


#This is to first display welcome to the user of the program
print( "Welcome!")

#This is for the user to input the company name
Company = input("Enter company name: ")

#This is the input for how much feet of fiber optic cable the user needs to be installed
Feet = float(input("Enter the number of feet of fiber optic cable: "))

#This is the fixed cost of 1 foot of fiber optic cable that'll be used for the equation.
Cost = 0.87

#This is the equation to calculate total cost of fiber optic cable user wishes to install
Total = Feet * Cost

#This is to print the receipt
#first is an extra line for space, second is the title receipt. third is the company name
#fourth is the amount of feet of fiber cable, and fifth is the grand total cost
print(" ")
print("Receipt:")
print("Company name: ", Company)
print("Installed amount of fiber optic cable by feet: ", Feet)
print("Grand total: ", Total)
