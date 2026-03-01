collection = input('Vvedit elementy 1 spysku zilyh chysel: ')
numbers = collection.split(', ')
numbers = [int(x) for x in numbers]
collection2 = []
for number in numbers:
    if number not in collection2:
        collection2.append(number)
print(collection2)