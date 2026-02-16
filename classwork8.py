# collection = list()
# collection =[]
# print(type(collection))
# collection = [10, 10.5, 'text', True]
#print(collection[0].upper())
#fruits = ['apple', 'lemon', 'pamelo', 'mango', 'pineapple']
# print(fruits[0])
# print(fruits[1:3]) #1-3
# print(fruits[:4]) #0-3
# print(fruits[1:]) #1-4
# print(fruits[1:4:2]) #1-3, step 2
# print(fruits[-1])
# print(fruits[-2:-5:-1])
# print(fruits[::-1])
# text = 'text'
# text[2] = u - error
# fruits[3] = 'kiwi' #mango - kiwi
# print(fruits)
# fruits_count = len(fruits)
# print(fruits_count)
# #print(len(fruits))
# counter = 0
# while counter < len(fruits):
#     print(fruits[counter].upper())
#     counter += 1
# for fruit in fruits:
#     print(fruit)
# #names = 'Anthony, Sergey, Anastesia, Ignat, Katherin'
# names = input('Vvedit imena cherez komu: ')
# names = names.split(', ')
# print(names)
# print(type(names))
# fruits = ['apple', 'lemon', 'pamelo', 'mango', 'pineapple', 'watermelon']
# fruits.append('kiwi')
# fruits.extend(['orange, banana'])
# fruits.insert(3, 'watermelon')
# fruits.pop(5)
# fruits.remove('watermelon')
# print(', '.join(fruits))
# apple_count = fruits.count('apple')
# print(apple_count)
# watermelon_count = fruits.count('watermelon')
# print(watermelon_count)
# grapefruit_count = fruits.count('grapefruit')
# print(grapefruit_count)

# while 'watermelon' in fruits:
#     fruits.remove('watermelon')
# print(', '.join(fruits))

# if 'grapefruit' in fruits:
#     fruits.remove('grapefruit')
# print(', '.join(fruits))
# print(fruits.index('watermelon'))
# print(fruits.index('pineapple'))
# #print(fruits.index('grapefruit')) - error
# fruits_copy = fruits.copy
# fruits_copy.append('grapefruit')
# print(fruits_copy)
# print(fruits)
# fruits.sort() #by alfabet
# fruits.reverse()
# print(fruits)
# list1 = [1, 2, 3]
# list2 = [5, 6, 7]
# result = list1 + list2
# print(result)
# print(list1 * 1)
# numbers = [10, 1, 2, 3, -6, 12, 0, -11, 5]
# even_numbers = []
# for number in numbers:
#     if number % 2 == 0:
#         even_numbers.append(number)
# print(even_numbers)
# even_numbers = [number for number in numbers if number % 2 == 0] #то же самое, но в одну строчку
# print(even_numbers)
# odd_numbers = [x for x in range(1, 20, 2)]
# print(odd_numbers)
list2d = [ [1, 3, 3], [4, 5, 6] ]
for list in list2d:
    for i in list:
        print(i, end=' ')
    print()
tuple1 = tuple()
print(type(tuple1))
fruits = ['apple', 'lemon', 'pamelo', 'mango', 'pineapple']
fruits_tuple = tuple(fruits)
print(type(fruits_tuple))
#fruits_tuple[2] = 'kjhg' - error, не можна змінювати
fruits_tuple = tuple['apple', 'orange']
print(fruits_tuple)
colors = ('red', 'green', 'blue', 'purple')
(red, green, blue, purple) = colors
(red, green, *other_colors) = colors
print(red)
print(green)
print(blue)
print(purple)
print(other_colors)