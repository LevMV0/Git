#1
num1 = int(input('Vvedit pershe chyslo: '))
num2 = int(input('Vvedit druge chyslo: '))
diapazon = num1
print(diapazon)
while diapazon != num2:
    diapazon += 1
    print(diapazon)
#2
num1 = int(input('Vvedit pershe chyslo: '))
num2 = int(input('Vvedit druge chyslo: '))
diapazon = num1
if diapazon % 2 == 0:
    print(diapazon)
while diapazon != num2:
    diapazon += 1
    if diapazon % 2 == 0:
        print(diapazon)
#3
num1 = int(input('Vvedit pershe chyslo: '))
num2 = int(input('Vvedit druge chyslo: '))
diapazon = num2
if diapazon % 2 == 0:
    print(diapazon)
while diapazon != num1:
    diapazon -= 1
    if diapazon % 2 == 0:
        print(diapazon)
#4
num1 = int(input('Vvedit pershe chyslo: '))
num2 = int(input('Vvedit druge chyslo: '))
poryadok = int(input('Oberit poradok(1- zrost, 2 - spad): '))
if poryadok == 1:
    diapazon = num1
    print(diapazon)
    while diapazon != num2:
        diapazon += 1
        print(diapazon)
elif poryadok == 2:
    diapazon = num2
    print(diapazon)
    while diapazon != num1:
        diapazon -= 1
        print(diapazon)
else:
    print('Nekorektniy poryadok')
#5
num1 = int(input('Vvedit pershe chyslo: '))
num2 = int(input('Vvedit druge chyslo: '))
if num1 < num2:
    diapazon = num1
    if diapazon % 2 != 0:
        print(diapazon)
    while diapazon != num2:
        diapazon += 1
        if diapazon % 2 != 0:
            print(diapazon)
if num1 > num2:
    diapazon = num2
    if diapazon % 2 != 0:
        print(diapazon)
    while diapazon != num1:
        diapazon += 1
        if diapazon % 2 != 0:
            print(diapazon)
#6
num1 = int(input('Vvedit pershe chyslo:'))
num2 = int(input('Vvedit druge chyslo:'))
if num1 < num2:
    diapazon = num1
    if diapazon % 2 == 0:
        print(diapazon)
    while diapazon != num2:
        diapazon += 1
        if diapazon % 2 == 0:
            print(diapazon)
    diapazon = num2
    if diapazon % 2 != 0:
        print(diapazon)
    while diapazon != num1:
        diapazon -= 1
        if diapazon % 2 != 0:
            print(diapazon)
if num1 > num2:
    diapazon = num2
    if diapazon % 2 == 0:
        print(diapazon)
    while diapazon != num1:
        diapazon += 1
        if diapazon % 2 == 0:
            print(diapazon)
    diapazon = num1
    if diapazon % 2 != 0:
        print(diapazon)
    while diapazon != num2:
        diapazon -= 1
        if diapazon % 2 != 0:
            print(diapazon)