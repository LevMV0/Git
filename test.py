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