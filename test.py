colection = input('Vvedit elementy spysku zilyh chysel: ')
unique = []
numbers = colection.split(', ')
numbers = [int(x) for x in numbers]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)