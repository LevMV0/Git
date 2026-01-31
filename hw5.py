#1
num1 = int(input("Vvedit pershe chyslo: "))
num2 = int(input("Vvedit druge chyslo: "))
chyslo = num1
if chyslo % 7 == 0:
    print (chyslo)
while chyslo != num2:
    chyslo += 1
    if chyslo % 7 == 0:
        print(chyslo)
#2
num1 = int(input("Vvedit pershe chyslo: "))
num2 = int(input("Vvedit druge chyslo: "))
diapazon = num1
print(diapazon)
while diapazon != num2:
    diapazon += 1
    print(diapazon)
diapazon = num2
print(diapazon)
while diapazon != num1:
    diapazon -= 1
    print(diapazon)
diapazon = num1
if diapazon % 7 == 0:
    print (diapazon)
while diapazon != num2:
    diapazon += 1
    if diapazon % 7 == 0:
        print(diapazon)
diapazon = num1
count = 0
if diapazon % 5 == 0:
    count += 1
while diapazon != num2:
    diapazon += 1
    if diapazon % 5 == 0:
        count += 1
print (count)
#3
num1 = int(input("Vvedit pershe chyslo: "))
num2 = int(input("Vvedit druge chyslo: "))
diapazon = num1
if diapazon % 3 == 0 and diapazon % 5 == 0:
    print (diapazon, "Fizz Buzz")
elif diapazon % 3 == 0:
    print (diapazon, "Fizz")
elif diapazon % 5 == 0:
    print(diapazon, "Buzz")
else:
    print (diapazon)
while diapazon != num2:
    diapazon += 1
    if diapazon % 3 == 0 and diapazon % 5 == 0:
        print(diapazon, "Fizz Buzz")
    elif diapazon % 3 == 0:
        print (diapazon, "Fizz")
    elif diapazon % 5 == 0:
        print(diapazon, "Buzz")
    else:
        print(diapazon)
#4
num1 = int(input("Vvedit pershe chyslo: "))
num2 = int(input("Vvedit druge chyslo: "))
interval = int(input("Vvedit interval: "))
poryadok = int(input("Oberit poryadok(1 - pryamyi, 2 - zvorotnii): "))
if poryadok == 1:
    diapazon = num1
    print(diapazon)
    while diapazon != num2:
        diapazon += interval
        print(diapazon)
elif poryadok == 2:
    diapazon = num2
    print(diapazon)
    while diapazon != num1:
        diapazon -= interval
        print(diapazon)
#5
num1 = int(input("Vvedit pershe chyslo: "))
num2 = int(input("Vvedit druge chyslo: "))
if num1 < num2:
    diapazon = num1
    if diapazon % 4 == 0 and diapazon % 6 != 0:
        print(diapazon)
    while diapazon != num2:
        diapazon += 1
        if diapazon % 4 == 0 and diapazon % 6 != 0:
            print(diapazon)
elif num1 > num2:
    diapazon = num2
    if diapazon % 4 == 0 and diapazon % 6 != 0:
        print(diapazon)
    while diapazon != num1:
        diapazon -= 1
        if diapazon % 4 == 0 and diapazon % 6 != 0:
            print(diapazon)
#6
A = int(input("Vvedit chyslo: "))
N = int(input("Vvedit stupin: "))
A2 = A
if N == 0:
    A2 = 1
    print(A2)
elif N > 0:
    stupin = 1
    while stupin != N:
        stupin += 1
        A2 *= A 
    print (A2)
elif N < 0 and A != 0:
    stupin = 1
    while stupin != -N:
        stupin += 1
        A2 *= A 
    print (1/A2)
elif N < 0 and A == 0:
    print("error")