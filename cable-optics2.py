#DSC 510
#Week 3
#Assignment 3.1
#Yitzchak Zweig
#3/27/25
#Program: Creating Fiber Optic Cost Calculator with "if" Statements

#Welcome Message
print ("Welcome to Steve's Cable Optics")

#Retrieve company name from user
company_name = input("Enter your company name: ")

#Retrieve the number of feet needed by use
feet_needed = float(input("Enter the amount of fiber optic feet needed: "))

#Make sure user input doesn't lead to ValueError (Ensure only positive numbers)
if feet_needed <= 0: print("Error. Please enter a valid amount of fiber optic feet.")


#Calculate price per foot
if feet_needed > 100: price_per_foot =.85
elif feet_needed > 250: price_per_foot = .75
elif feet_needed > 500: price_per_foot = .55
else: price_per_foot = .95

#Calculate cost
total_cost = feet_needed * price_per_foot

#Print receipt
print(company_name)
print("Feet needed - ")
print(feet_needed )
print("Price - ")
print(price_per_foot)
print("total cost - ")
print (total_cost)

