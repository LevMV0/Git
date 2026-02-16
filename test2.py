colection = input('Vvedit elementy spysku zilyh chysel: ')
sum = 0
numbers = colection.split(', ')
numbers = [int(x) for x in numbers]
for number in numbers:
    if number % 2 == 0:
        sum += number
print(sum)