#1
num1 = float(input("Введіть скільки секунд минуло з початку дня: "))
od = (input("Введіть у яких одиницях ви хочете порахувати час, що залишився до кінця дня(sec, min, hours): "))
if od == 'sec':
    print(f'(24 * 3600) - {num1} = {(24 * 3600) - num1}')
if od == 'min':
    print(f'(24 * 60) - ({num1} / 60) = {(24 * 60) - (num1 / 60)}')
if od == 'hours':
    print(f'24 - ({num1}/3600) = {24 - (num1 / 3600)}')
#2
diam = float(input("Введіть діаметр кола: "))
pi = 3,14
count = (input("Введітьб що хочете порахувати(S - площа або P - периметр)"))
if count == "S":
    print(f'({diam}/2 ** 2) * {pi} = {(diam/2) **2 * pi}')
else:
    print(f'{diam} * {pi} = {diam * pi}')