#1
num = int(input("Vvedit chyslo: "))
mnozhennya = int
for mnozhennya in range(11):
    print(f'{num} * {mnozhennya} = {num * mnozhennya}')
#2
for num in range(10):
    for mnozhennya in range(11):
        print(f'{num} * {mnozhennya} = {num * mnozhennya}')
#3
N = int(input("Skilky chysel vy hochete vvesty? "))
max_num = int(input("Vvedite chyslo: "))
for i in range (N-1):
    num = int (input("Vvedite chyslo: "))
    if num > max_num:
        max_num = num
print(f'max_num = {max_num}')
#4
import random
random_number = random.randint(1, 500)
num = int(input("Vgadai chyslo: "))
popytki = 0
for i in range(500):
    if num == random_number:
        popytki += 1
        print("Chyslo vgadano!")
        break
    if num == 0:
        break
    if num > random_number:
        popytki += 1
        print("Chyslo bilshe zagadanogo")
        num = int(input("Vgadai chyslo: "))
        continue
    if num < random_number:
        popytki += 1
        print("Chyslo menshe zagadanogo")
        num = int(input("Vgadai chyslo: "))
        continue
print(f'Kilkist popytok: {popytki}')
#5
figura = input("Oberit figuru(kvadrat abo praymokutnyk): ")
symvol = input("Oberit symvol: ")
if figura == 'kv':
    storona = int(input("Vvedit dovzhynu storony: "))
    for i in range(storona):
        print(symvol * storona)
elif figura == 'pr':
    shyryna = int(input("Vvedit shyrynu: "))
    vysota = int(input("Vvedit vysoty: "))
    for i in range(vysota):
       print(symvol * shyryna)