'''
a = 100
b = 50
# if a > b: print ("a більше b")
print ("a > b") if a > b else print ("a < b")
# -1 - унарний оперантор
# 10 + 5 - бінарний оператор
# age = 17
# can_vote = age >= 18 ? True: False - тринарний оператор
login = input("Введіть ваш логін: ")
display_name = login if login else "Гість"
print(f'Hello, {display_name}')

age = 17
if age < 18:
    pass # TODO: Implement underage logic later
else:
    print("Full access granted")

day = int(input("Введіть номер дня тижня"))
match day:
    case 1: print("Понеділок")
    case 2: print("Вівторок")
    case 3: print("Середа")
    case 4: print("Четвер")
    case 5: print("П\'ятниця")
    case 6: print("Субота")
    case 7: print("Неділя")
    case _: print("Некоректний номер дня")


if day == 1:
    print("Понеділок")
elif day == 2:
    print("Вівторок")
elif day == 3:
    print("Середа")
elif day == 4:
    print("Четвер")
elif day == 5:
    print("П\'ятниця")
elif day == 6:
    print("Субота")
elif day == 7:
    print("Неділя")
else:
    print("Неможливий номер")

month = int(input("Введіть номер місяця"))
match month:
    case 12 | 1 | 2: print("Зима")
    case 3 | 4 | 5: print("Весна")
    case 6 | 7 | 8: print("Літо")
    case 9 | 10 | 11: print("Осінь")
    case _: print("Некоректний номер місяця")
    
month = int(input("Введіть номер місяця"))
day = int(input("Введіть номер дня тижня"))
match month:
    case  1 | 2 | 3 | 4 | 5 if mont == 12:
        print("будній день грудня")
    case  1 | 2 | 3 | 4 | 5 if month == 1:
        print("будній день січня")
    case  6 | 7 if month == 12:
        print("вихідний грудня")
    case  6 | 7 if month == 1:
        print("вихідний січня")
        '''

