num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
sa = (num1+num2)/2 #sa - середнє арифметичне
operation = (input("Введіть операцію: "))
if operation == "+" :
    print(f'{num1} + {num2} = {num1 + num2}')
elif operation == "-" :
    print(f'{num1} - {num2} = {num1 - num2}')
elif operation == "*" :
    print(f'{num1} * {num2} = {num1 * num2}')
elif operation == 'sa': 
    print(sa)
else:
    print('Некоректна операція')