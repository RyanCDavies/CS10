NUM_EMPLOYEES = 6

employee_hours = []
gross_pay = 0

for i in range(NUM_EMPLOYEES):
    user_value = int(input("Enter the hours worked by employee " + str(i+1) + ': '))
    employee_hours.append(user_value)
    
print('')
pay_rate = float(input('Enter the hourly pay rate: '))
print('')

for i in range (NUM_EMPLOYEES):
    print('Grosss pay for employee ', i+1, ': $', format(employee_hours[i] * pay_rate, '.2f'), sep='')    
