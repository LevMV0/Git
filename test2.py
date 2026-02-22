colection1 = input('Vvedit elementy 1 spysku zilyh chysel: ')
colection2 = input('Vvedit elementy 2 spysku zilyh chysel: ')
numbers1 = colection1.split(', ')
numbers2 = colection2.split(', ')
numbers1 = [int(x) for x in numbers1]
numbers2 = [int(x) for x in numbers2]
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
