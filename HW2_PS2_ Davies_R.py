#Ryan Davies
#1255293
#Homework 2 Program Set 2
#calculates 2017 and 2018 taxes from user input and sends their values, differences, and the input as output, will loop forever until given a negative number

#gets the income from the user
income = float(input("Enter income as an integer with no commas: "))

#2017 tax calculation
while (income >= 0):
    if (income <= 9325):
        tax17 = income*.10
    elif (income <= 37950):
        tax17 = 9325*.10 + (income-9325)*.15
    elif (income <= 91900):
        tax17 = 9325*.10 + 28625*.15 + (income-37950)*.25
    elif (income <= 191650):
        tax17 = 9325*.10 + 28625*.15 + 53950*.25 + (income-91900)*.28
    elif (income <= 416700):
        tax17 = 9325*.10 + 28625*.15 + 53950*.25 + 99750*.28 + (income-191650)*.33
    elif (income <= 418400):
        tax17 = 9325*.10 + 28625*.15 + 53950*.25 + 99750*.28 + 225050*.33 + (income-416700)*.35
    else:
        tax17 = 9325*.10 + 28625*.15 + 53950*.25 + 99750*.28 + 225050*.33 + 1700*.35 + (income-418400)*.396     

    #2018 tax calculation
    if (income <= 9525):
        tax18 = income*.10
    elif (income <= 38700):
        tax18 = 9525*.10 + (income-9525)*.12
    elif (income <= 82500):
        tax18 = 9525*.10 + 29175*.12 + (income-38700)*.22
    elif (income <= 157500):
        tax18 = 9525*.10 + 29175*.12 + 43800*.22 + (income-825700)*.24
    elif (income <= 200000):
        tax18 = 9525*.10 + 29175*.12 + 43800*.22 + 75000*.24 + (income-157500)*.32
    elif (income <= 500000):
        tax18 = 9525*.10 + 29175*.12 + 43800*.22 + 75000*.24 + 42500*.32 + (income-200000)*.35
    else:
        tax18 = 9525*.10 + 29175*.12 + 43800*.22 + 75000*.24 + 42500*.32 + 300000*.35 + (income-500000)*.37   

    #difference calc
    percentDifference = ((tax18-tax17)/(tax17))*100
    if (percentDifference < 0):
        percentDifference = percentDifference * -1

    #output
    print('Income:', format(income, '.0f'))
    print('2017 tax:', format(tax17, '.2f'))
    print('2018 tax:', format(tax18, '.2f'))
    print('Difference:', format((tax18 - tax17), '.2f'))
    print('Difference (percent):', format(percentDifference, '.2f'), sep='')
    print('')

    #input again
    income = float(input("Enter income as an integer with no commas: "))
    
##TEST RUN 1##
##Enter income as an integer with no commas: 8000
##Income: 8000
##2017 tax: 800.00
##2018 tax: 800.00
##Difference: 0.00
##Difference (percent):0.00
##
##Enter income as an integer with no commas: 15000
##Income: 15000
##2017 tax: 1783.75
##2018 tax: 1609.50
##Difference: -174.25
##Difference (percent):9.77
##
##Enter income as an integer with no commas: 40000
##Income: 40000
##2017 tax: 5738.75
##2018 tax: 4739.50
##Difference: -999.25
##Difference (percent):17.41
##
##Enter income as an integer with no commas: 100000
##Income: 100000
##2017 tax: 20981.75
##2018 tax: -160078.50
##Difference: -181060.25
##Difference (percent):862.94
##
##Enter income as an integer with no commas: 200000
##Income: 200000
##2017 tax: 49399.25
##2018 tax: 45689.50
##Difference: -3709.75
##Difference (percent):7.51
##
##Enter income as an integer with no commas: 500000
##Income: 500000
##2017 tax: 153818.85
##2018 tax: 150689.50
##Difference: -3129.35
##Difference (percent):2.03
##
##Enter income as an integer with no commas: 1000000
##Income: 1000000
##2017 tax: 351818.85
##2018 tax: 335689.50
##Difference: -16129.35
##Difference (percent):4.58
##
##Enter income as an integer with no commas: 10000000
##Income: 10000000
##2017 tax: 3915818.85
##2018 tax: 3665689.50
##Difference: -250129.35
##Difference (percent):6.39
##
##Enter income as an integer with no commas: -1

##TEST RUN 2##
##Enter income as an integer with no commas: -1

##TEST RUN 3##
##Enter income as an integer with no commas: 12345
##Income: 12345
##2017 tax: 1385.50
##2018 tax: 1290.90
##Difference: -94.60
##Difference (percent):6.83
##
##Enter income as an integer with no commas: 234
##Income: 234
##2017 tax: 23.40
##2018 tax: 23.40
##Difference: 0.00
##Difference (percent):0.00
##
##Enter income as an integer with no commas: 20000
##Income: 20000
##2017 tax: 2533.75
##2018 tax: 2209.50
##Difference: -324.25
##Difference (percent):12.80
##
##Enter income as an integer with no commas: 50000
##Income: 50000
##2017 tax: 8238.75
##2018 tax: 6939.50
##Difference: -1299.25
##Difference (percent):15.77
##
##Enter income as an integer with no commas: 4000
##Income: 4000
##2017 tax: 400.00
##2018 tax: 400.00
##Difference: 0.00
##Difference (percent):0.00
##
##Enter income as an integer with no commas: 60000000
##Income: 60000000
##2017 tax: 23715818.85
##2018 tax: 22165689.50
##Difference: -1550129.35
##Difference (percent):6.54
##
##Enter income as an integer with no commas: -9

##TEST RUN 4##
##Enter income as an integer with no commas: 200000
##Income: 200000
##2017 tax: 49399.25
##2018 tax: 45689.50
##Difference: -3709.75
##Difference (percent):7.51
##
##Enter income as an integer with no commas: 9000000
##Income: 9000000
##2017 tax: 3519818.85
##2018 tax: 3295689.50
##Difference: -224129.35
##Difference (percent):6.37
##
##Enter income as an integer with no commas: 1452888
##Income: 1452888
##2017 tax: 531162.50
##2018 tax: 503258.06
##Difference: -27904.44
##Difference (percent):5.25
##
##Enter income as an integer with no commas: 120000
##Income: 120000
##2017 tax: 26581.75
##2018 tax: -155278.50
##Difference: -181860.25
##Difference (percent):684.15
##
##Enter income as an integer with no commas: 36000
##Income: 36000
##2017 tax: 4933.75
##2018 tax: 4129.50
##Difference: -804.25
##Difference (percent):16.30
##
##Enter income as an integer with no commas: -1

##TEST RUN 5##
##Enter income as an integer with no commas: 10
##Income: 10
##2017 tax: 1.00
##2018 tax: 1.00
##Difference: 0.00
##Difference (percent):0.00
##
##Enter income as an integer with no commas: 20000000
##Income: 20000000
##2017 tax: 7875818.85
##2018 tax: 7365689.50
##Difference: -510129.35
##Difference (percent):6.48
##
##Enter income as an integer with no commas: 12560000000
##Income: 12560000000
##2017 tax: 4973715818.85
##2018 tax: 4647165689.50
##Difference: -326550129.35
##Difference (percent):6.57
##
##Enter income as an integer with no commas: 23456
##Income: 23456
##2017 tax: 3052.15
##2018 tax: 2624.22
##Difference: -427.93
##Difference (percent):14.02
##
##Enter income as an integer with no commas: 1289000
##Income: 1289000
##2017 tax: 466262.85
##2018 tax: 442619.50
##Difference: -23643.35
##Difference (percent):5.07
##
##Enter income as an integer with no commas: 5637000
##Income: 5637000
##2017 tax: 2188070.85
##2018 tax: 2051379.50
##Difference: -136691.35
##Difference (percent):6.25
##
##Enter income as an integer with no commas: 9
##Income: 9
##2017 tax: 0.90
##2018 tax: 0.90
##Difference: 0.00
##Difference (percent):0.00
##
##Enter income as an integer with no commas: -1
