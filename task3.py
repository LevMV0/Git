#1
num = float(input("Введіть число: "))
if (num % 2) == 0:
    print("Even number")
else:
    print("Odd number")
#2
num = float(input("Введіть число: "))
if (num % 7) == 0:
    print("Number is multiple 7")
else:
    print("Number is not multiple 7")
#3
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
if num1 > num2:
    print(num1,">",num2)
elif num2 > num1:
    print(num2, ">", num1)
else:
    print(num1,"=",num2)
#4
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
if num1 < num2:
    print(num1,"<",num2)
elif num2 > num1:
    print(num2, "<", num1)
else:
    print(num1,"=",num2)
#5
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
#6
suma = float(input('Введіть суму у доларах: '))
valuta = (input("EUR, GBR, UAH? "))
kurs = float(input("Введіть курс валюти по відношенню до долара: "))
print(f'{suma} * {kurs} = {suma * kurs}')
