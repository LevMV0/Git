#1
numbers_input = input("Vvedit spysok chysel: ")
n = int(input("Vvedit kilkist pozytsii N: "))
numbers = [int(x) for x in numbers_input.split(', ')]
shifted = numbers[-n:] + numbers[:-n]
print(shifted)
#2.1
colection1 = input('Vvedit elementy 1 spysku zilyh chysel: ')
colection2 = input('Vvedit elementy 2 spysku zilyh chysel: ')
numbers1 = colection1.split(', ')
numbers2 = colection2.split(', ')
numbers1 = [int(x) for x in numbers1]
numbers2 = [int(x) for x in numbers2]
colection3 = numbers1 + numbers2
print(colection3)
#2.2
colection3 = numbers1 + numbers2
unique = []
for number in colection3:
    if number not in unique:
        unique.append(number)
print(unique)
#1.3
common = []
for number in numbers1:
    if number in numbers2 and number not in common:
        common.append(number)
colection3 = common
print(colection3)
#2.4
unique1 = []
for number in numbers1:
    if number not in unique1:
        unique1.append(number)
unique2 = []
for number in numbers2:
    if number not in unique2:
        unique2.append(number)
colection3 = unique1 + unique2
print(colection3)
#2.5
colection3 = []
max1 = max(numbers1)
min1 = min(numbers1)
max2 = max(numbers2)
min2 = min(numbers2)
colection3.append(max1)
colection3.append(max2)
colection3.append(min1)
colection3.append(min2)
print(colection3)