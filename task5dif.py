#1
num1 = int(input('Vvedit pershe chyslo: '))
num2 = int(input('Vvedit druge chyslo: '))
diapazon = num1
print(diapazon)
sum = diapazon
kilkist = 2
while diapazon != num2:
    diapazon += 1
    print(diapazon)
    sum = sum + diapazon
    kilkist += 1
print(f'Sum = {sum}')
print(f'kilkist = {kilkist}')
print(f'S = {sum/kilkist}')
#2
num = int(input('Vvedit chyslo: '))
a = 1
while a != num:
 a = a * (a+1)
print (a)