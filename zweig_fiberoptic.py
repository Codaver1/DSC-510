#Program: Fiber Optic Cost
#Class: DSC 510 (Alsaleem)
#Assignment 2.1
#Author: Yitzchak Zweig
#Date 3/21/25


#Welcome Message
print ("Welcome to Charlie Sheens [no relation] fiber optics megastore")

#Get customer's name
company_name =  input("Enter company name:")

#Get the amount of cable
cable_amount = input("Enter cable amount:")

cable = float(cable_amount)
cost = .95

#Calculate cost
print (cost*cable)

#Print Receipt
print ("Charlie Sheens Fiber Optic Cable Megastore Receipt")
print (company_name)
print ("cost per foot = .95")
print (cable_amount)
print ("Total cost = "), print (cost*cable)