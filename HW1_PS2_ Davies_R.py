#Ryan Davies
#1255293
#Homework 1 Program Set 2
#This program asks for data on stock purchases and selling, then calculates how much was paid and lost through selling it

#input
STOCK_NAME = input("Enter stock name: ")
NUM_SHARES = int(input("Enter number of shares: "))
PURCHASE_PRICE = float(input("Enter purchase price: "))
SELL_PRICE = float(input("Enter selling price: "))
COMMISSION = float(input("Enter commission: "))

#calc
AMT_PAID = NUM_SHARES * PURCHASE_PRICE
COMMISSION_PURCHASE = AMT_PAID * COMMISSION
AMT_SOLD = NUM_SHARES * SELL_PRICE
COMMISSION_SALE = AMT_SOLD * COMMISSION
PROFIT = AMT_SOLD - AMT_PAID - COMMISSION_SALE - COMMISSION_PURCHASE

#output
print('')
print('Amount paid for the stock:          $', format(AMT_PAID, '13,.2f'), sep ='')
print('Commission paid on the purchase:    $', format(COMMISSION_PURCHASE, '13,.2f'), sep ='')
print('Amount the stock sold for:          $', format(AMT_SOLD, '13,.2f'), sep ='')
print('Commission paid on the sale:        $', format(COMMISSION_SALE, '13,.2f'), sep ='')
print('Profit (or loss if negative):       $', format(PROFIT, '13,.2f'), sep ='')

##Test Run 1
##Enter stock name: Kaplack, Inc.
##Enter number of shares: 10000
##Enter purchase price: 33.92
##Enter selling price: 35.92
##Enter commission: 0.04
##
##Amount paid for the stock:          $   339,200.00
##Commission paid on the purchase:    $    13,568.00
##Amount the stock sold for:          $   359,200.00
##Commission paid on the sale:        $    14,368.00
##Profit (or loss if negative):       $    -7,936.00

##Test Run 2
##Enter stock name: IBM
##Enter number of shares: 15000
##Enter purchase price: 50.25
##Enter selling price: 100.20
##Enter commission: 0.02
##
##Amount paid for the stock:          $   753,750.00
##Commission paid on the purchase:    $    15,075.00
##Amount the stock sold for:          $ 1,503,000.00
##Commission paid on the sale:        $    30,060.00
##Profit (or loss if negative):       $   704,115.00

##Test Run 3
##Enter stock name: microsoft
##Enter number of shares: 1200
##Enter purchase price: 37.25
##Enter selling price: 40.12
##Enter commission: .03
##
##Amount paid for the stock:          $    44,700.00
##Commission paid on the purchase:    $     1,341.00
##Amount the stock sold for:          $    48,144.00
##Commission paid on the sale:        $     1,444.32
##Profit (or loss if negative):       $       658.68

##Test Run 4
##Enter stock name: walmart
##Enter number of shares: 1450
##Enter purchase price: 44.23
##Enter selling price: 41.92
##Enter commission: .01
##
##Amount paid for the stock:          $    64,133.50
##Commission paid on the purchase:    $       641.33
##Amount the stock sold for:          $    60,784.00
##Commission paid on the sale:        $       607.84
##Profit (or loss if negative):       $    -4,598.67

##Test Run 5
##Enter stock name: nintendo
##Enter number of shares: 200
##Enter purchase price: 28.50
##Enter selling price: 33.67
##Enter commission: .03
##
##Amount paid for the stock:          $     5,700.00
##Commission paid on the purchase:    $       171.00
##Amount the stock sold for:          $     6,734.00
##Commission paid on the sale:        $       202.02
##Profit (or loss if negative):       $       660.98
