#1
collection = input('Vvedit elementy 1 spysku zilyh chysel: ')
numbers = collection.split(', ')
numbers = [int(x) for x in numbers]
collection2 = []
for number in numbers:
    if number not in collection2:
        collection2.append(number)
print(collection2)
#2
import random
set1 = set(random.randint(1, 20) for _ in range(10))
set2 = set(random.randint(1, 20) for _ in range(10))
print('Mnozhyna1: ', set1)
print('Mnozhyna2: ', set2)
print('Ob\'yednannya: ', set1 | set2)
print('Riznycya: ', set1 - set2)
print('Peretyn: ', set1 & set2)
#3
word1 = input('Vvedit pershe slovo: ').lower()
word2 = input('Vvedit druge slovo: ').lower()
if set(word1) == set(word2):
    print('Slova mayut odnakovi mnozhyny bukv')
else:
    print('Slova ne mayut odnakovi mnozhyny bukv')