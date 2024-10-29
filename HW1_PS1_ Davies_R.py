#Ryan Davies
#1255293
#Homework 1 Program Set 1
#This program calculates and returns monthly and total payments on a loan with a fixed interest rate

#input
ANNUAL_INTEREST_RATE = float(input("Enter annual interest rate, (e.g., 7.25) : "))
NUMBER_OF_YEARS = int(input("Enter number of years as an integer, (e.g., 5) : "))
LOAN_AMOUNT = float(input("Enter loan amount, (e.g., 120000.95) : "))

#calc
MONTHLY_INTEREST_RATE = ANNUAL_INTEREST_RATE / 1200
MONTHLY_PAYMENT = LOAN_AMOUNT * MONTHLY_INTEREST_RATE / (1 - 1/(1 + MONTHLY_INTEREST_RATE)**(NUMBER_OF_YEARS * 12))
TOTAL_PAYMENT = MONTHLY_PAYMENT * NUMBER_OF_YEARS *12

#output
print("The monthly payment is",format(MONTHLY_PAYMENT, ',.2f'))
print("The total payment is", format(TOTAL_PAYMENT, ',.2f'))

##Test Run 1
##Enter annual interest rate, (e.g., 7.25) : 4.5
##Enter number of years as an integer, (e.g., 5) : 30
##Enter loan amount, (e.g., 120000.95) : 350000.50
##The monthly payment is 1,773.40
##The total payment is 638,424.40

##Test Run 2
##Enter annual interest rate, (e.g., 7.25) : 2.7
##Enter number of years as an integer, (e.g., 5) : 15
##Enter loan amount, (e.g., 120000.95) : 12000.45
##The monthly payment is 81.15
##The total payment is 14,607.44

##Test Run 3
##Enter annual interest rate, (e.g., 7.25) : 7.25
##Enter number of years as an integer, (e.g., 5) : 5
##Enter loan amount, (e.g., 120000.95) : 120000.95
##The monthly payment is 2,390.34
##The total payment is 143,420.54

##Test Run 4
##Enter annual interest rate, (e.g., 7.25) : 4.57
##Enter number of years as an integer, (e.g., 5) : 6
##Enter loan amount, (e.g., 120000.95) : 12345.67
##The monthly payment is 196.37
##The total payment is 14,138.86

##Test Run 5
##Enter annual interest rate, (e.g., 7.25) : 9.02
##Enter number of years as an integer, (e.g., 5) : 60
##Enter loan amount, (e.g., 120000.95) : 567890.67
##The monthly payment is 4,288.17
##The total payment is 3,087,484.54
