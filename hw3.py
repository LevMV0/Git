#1
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))
operation = (input("Введіть операцію: "))
if operation == "+":
    print(f'{num1} + {num2} = {num1 + num2}')
elif operation == "*":
    print(f'{num1} * {num2} * {num3} = {num1 * num2 * num3}')
else:
    print('Некоректна операція')
#2
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))
sa = (num1+num2+num3)/3 #sa - середнє арифметичне
operation = (input("Введіть операцію: "))
if operation == "max" :
    print(max(num1, num2, num3))
elif operation == 'min':
    print(min(num1, num2, num3))
elif operation == 'sa': 
    print(sa)
else:
    print('Некоректна операція')
#3
grade = float(input("Введіть оцінку(1, 2, 3, 4, 5): "))
if grade == 5:
    print("Відмінно")
elif grade == 4:
    print("Добре")
elif grade == 3:
    print("Задовільно")
elif grade == 2:
    print("Погано")
elif grade == 1:
    print("Дуже погано")
else:
    print("Помилка")
#4
num = float(input("Введіть кількість метрів: "))
od = (input("Оберіть, в які одиниці бажаєте перевести: ")) #od - одиниці
if od == 'mi':
     print(f'У мілях = {num1 * 0.000621}')
elif od == 'in':
    print(f'У дюймах = {num1 * 39.37}')
elif od == 'yd':
    print(f'У ярдах = {num1 * 1.0936}')
elif od == 'mi, in, yd':
    print(f'У мілях = {num1 * 0.000621}; У дюймах = {num1 * 39.37}; У ярдах = {num1 * 1.0936}')
elif od == 'cm, km':
    print(f'У мілях = {num1 * 100}; У дюймах = {num1 / 100}')
else:
    print("Помилка")
#5
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operation = (input("Введіть операцію: "))
if operation == "+" :
    print(f'{num1} + {num2} = {num1 + num2}')
elif operation == "-" :
    print(f'{num1} - {num2} = {num1 - num2}')
elif operation == "*" :
    print(f'{num1} * {num2} = {num1 * num2}')
elif operation == '/': 
    print(f'{num1} / {num2} = {num1 / num2}')
elif operation == '%': 
    print(f'{num1} % {num2} = {num1 % num2}')
elif operation == '**': 
    print(f'{num1} ** {num2} = {num1 ** num2}')
else:
    print('Некоректна операція')
#6
num1 = int(input("Введіть тризначне число: "))
if num1 % 111 == 0:
    print("Цифри однакові")
else:
    print("Цифри різні")
