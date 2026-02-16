#1
colection = input('Vvedit elementy spysku zilyh chysel: ')
numbers = colection.split(', ')
numbers = [ int(x) for x in numbers]
print(sum(numbers), sum(numbers)/len(numbers))
#2
colection = input('Vvedit elementy spysku zilyh chysel: ')
count = 0
numbers = colection.split(', ')
for number in numbers:
    count += 1
print(count)
#3
colection = input('Vvedit elementy spysku zilyh chysel: ')
sum = 0
numbers = colection.split(', ')
numbers = [int(x) for x in numbers]
for number in numbers:
    if number % 2 == 0:
        sum += number
print(sum)
#4
colection = input('Vvedit elementy spysku zilyh chysel: ')
numbers = colection.split(', ')
numbers = [int(x) for x in numbers]
for index in range(len(numbers)):
    if numbers[index] % 2 == 0:
        print(index)
#5
colection = input('Vvedit elementy spysku zilyh chysel: ')
unique = []
numbers = colection.split(', ')
numbers = [int(x) for x in numbers]
for number in numbers:
    if number not in unique:
        unique.append(number)
print(unique)