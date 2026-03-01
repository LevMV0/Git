my_set = set()
my_set = set( ['apple', 'cherry', 'mango'] )

my_set = { 'apple', 'cherry', 'mango', 'mango' }

print(my_set)
print(type(my_set))

# print(my_set[0])
# my_set[1] = 'pamelo'

print(len(my_set))

new_set = {True, 1, 0, False}
print(len(new_set))
print(new_set)

for item in my_set:
    print(item)

print('apple' in my_set)
print('banana' not in my_set)





first = {'apple', 'mango', 'cherry', 'kiwi'}
second = {'mango', 'pamelo', 'kiwi', 'orange'}
union = first.union(second)
union = first | second #operator or
print(union)
print(first)
print(second)
intersection = first.intersection(second)
intersection = first & second #operator &
difference = first.difference(second) #first - second
difference = first - second
first.difference_update(second)
sym_diff = first.symmetric_difference(second)
sym_diff = first ^ second #operator XOR
first.symmetric_difference_update(second)
frozen_food = frozenset(first | second)
#frozen_food.add('watermelon') error!
new_dictionary = dict()
new_dictionary = {
    'key':'value',
    10:15.8
}
user = {
    'username':'admin',
    'age': 29
}
contacts = {
    'Anton':'0506959068',
    'Liza':'0474838458',
    'Sergii':'0550404033'
}
contacts['Sergii'] = '937465783'
contacts['Nastya'] = '3989486776' #adding Nastya
contacts.update({'Anton':'28796536', 'Tymofii':'3456783456'}) #new Anton number + adding Tymofii
print(contacts.keys())
print(contacts.values())
print(contacts.items())
for i in contacts:
    print(f'{i}:{contacts{i}}')
contacts.pop('Nastya')
contacts.popitem()
contacts.clear()
contacts_copy = contacts.copy()
employees = {
    '1':{
        'name':'Anton',
        'position':'Junior .NET Developer',
        'salary':'20000'
    },
    '2':{
        'name':'Anastesia',
        'position':'Team Lead',
        'salary':'115000'
    },
    '1':{
        'name':'Kyrylo',
        'position':'Senior .NET Developer',
        'salary':'90000'
    }
}
print(employees['2']['position'])


