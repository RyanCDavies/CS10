#Ryan Davies
#1255293
#Homework 3 Program Set 1
#This program asks for data on stock purchases and selling, then calculates how much was paid and lost through selling it

#input
stockName = input("Enter stock name: ")
numShares = int(input("Enter number of shares: "))
price = float(input("Enter purchase price: "))
sellPrice = float(input("Enter selling price: "))
commission = float(input("Enter commission: "))

#calc
amtPaid = numShares * price
commissionPurchase = amtPaid * commission
amtSold = numShares * price
commissionSale = amtSold * commission
profit = amtSold - amtPaid - commissionSale - commissionPurchase

#output
print('')
print('Amount paid for the stock:          $', format(amtPaid, '13,.2f'), sep ='')
print('Commission paid on the purchase:    $', format(commissionPurchase, '13,.2f'), sep ='')
print('Amount the stock sold for:          $', format(amtSold, '13,.2f'), sep ='')
print('Commission paid on the sale:        $', format(commissionSale, '13,.2f'), sep ='')
print('Profit (or loss if negative):       $', format(profit, '13,.2f'), sep ='')
