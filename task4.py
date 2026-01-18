#1
grade = float(input("Введіть бал за іспит: "))
if grade <= 100 and grade >= 90:
    print ("Відмінно")
elif grade <= 89 and grade >= 70:
    print ("Добре")
elif grade <= 69 and grade >= 50:
    print ("Задовільно")
elif grade < 50:
    print ("Незадовільно")
else:
    print ("Error")
#2
salary = int(input("Введіть заробітну плату: "))
experience = int (input("Введіть кількість років стажу: "))
if experience < 1:
    print('Премія не передбачена')
elif experience >=1 and experience < 3:
    print(f'премія 5% від зарплати = {salary/100 * 5}')
elif experience >= 3 and experience < 5:
    print(f'премія 10% від зарплати = {salary/100 * 10}')
elif experience >= 5:
    print(f'премія 15% від зарплати = {salary/100 * 15}')
#3
num = int(input('Введіть 4 значне число: '))
a = num % 10
b = num % 100
c = num % 1000
d = num % 10000
sum = a + (b - a)/10 + (c - b)/100 + (d - c)/1000
if sum % 2 == 0:
    print('Сума цифр парна')
else:
    print('Сума цифр непарна')
#4
num = int(input('Введіть 6 значне число: '))
a = num % 10
b = num % 100
c = num % 1000
d = num % 10000
e = num % 100000
f = num % 1000000
sum1 = a + (b - a)/10 + (c - b)/100
sum2 = (d - c)/1000 + (e - d)/10000 + (f - e)/100000
if (f/100000) > 1 and (f/100000) < 10 and sum1 == sum2:
    print('щасливе число')
elif (f/100000) > 1 and (f/100000) < 10 and sum1 != sum2:
    print("нещасливе число")
else:
    print("Error")
#5
num = int(input('Введіть 6 значне число: '))
a = num % 10
b = num % 100
c = num % 1000
d = num % 10000
e = num % 100000
f = num % 1000000
a1 = a
b1 = (b - a)/10
c1 = (c - b)
d1 = (d - c)
e1 = (e - d)/10000
f1 = (f - e)/100000
if (f/100000) >= 1 and (f/100000) < 10:
    print(f'num2 = {a1 * 100000 + b1 * 10000 + c1 + d1 + e1 * 10 + f1}')
else:
    print("Error")