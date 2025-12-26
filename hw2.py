#1
num1 = float (input("Enter first number"))
num2 = float(input("Enter second number"))
num3 = float(input("Enter third number"))
print (f"num1 + num2 + num3 = {num1 + num2 + num3}")
print (f"num1 * num2 * num3 = {num1 * num2 * num3}")
#2
d1 = float (input("Введіть довжину першої діагоналі"))
d2 = float(input("Введіть довжину другої діагоналі"))
print (f"(d1 * d2)/2 = {(d1 * d2)/2}")
#3 
num1 = float (input("Введіть зарплатню"))
num2 = float(input("Введіть суму щомісячного платежу за кредит"))
num3 = float(input("Введіть суму заборгованості за комунальні послуги"))
print (f"У вас залишається: {num1 - num2 - num3}")
#4
num1 = float (input("Введіть відстань поїздки у км"))
num2 = float(input("Введіть витрату палива на 100 км"))
num3 = float(input("Введіть ціну за 1 л палива"))
print (f"Витрата палива на 1 км: {num2/100}")
print (f"Вартість поїздки: {num1 * num2/100 *num3 }")
#5
num1 = float (input("Введіть загальну суму"))
num2 = float (input("Введіть кількість осіб"))
print (f"Сума чайових: {num1 * 15/100}")
print ((f"Загальна сума з чайовими: {num1 + (num1 * 15/100)}"))
print ((f"Кожен повинен заплатити: {(num1 + (num1 * 15/100))/num2}"))
#6
num1 = float(input("Вартість оренди за 1 день"))
num2 = float(input("Введіть кількість днів оренди"))
num3 = float(input("Введіть суму застави"))
print ((f"Загальна вартість оренди без застави: {num1 * num2}"))
print ((f"Загальна вартість оренди з урахуванням застави: {(num1 * num2) + num3}"))
print (f"Вартість оренди за один день: {(num1 * num2 - num3)/num2}")