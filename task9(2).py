#1
contacts = {}
while True:
    print('Oberit diyu(1 - dodaty contact, 2 - vydalyty contact, 3 - zminyty contact, 4 - pokazaty usi contacts, 0 -vyity): ')
    diya = input()
    if diya == '1':
        name = input('Vvedit im\'ya: ')
        number = input('Vvedit nomer telefonu: ')
        contacts[name] = number
        print(f'contact {name} zberezheno!')
    elif diya == '2':
        name = input('Vvedit im\'ya: ')
        if name in contacts:
            del contacts[name]
            print(f'contact {name} vydaleno')
        else:
            print(f'contactu {name} ne isnuye')
    elif diya == '3':
        name = input('Vvedit im\'ya: ')
        if name in contacts:
            new_number = input('Vvedit noviy number: ')
            contacts[name] = new_number
            print(f'contact {name} zmineno')
        else:
            print(f'contactu {name} ne isnuye')
    elif diya == '4':
        print(contacts)
    elif diya == '0':
        print('Vyhid')
        break
    else:
        print('Nevirna diya')
#2
text = input('Vvedit text: ')
text1 = text.lower()
words = text1.split(' ')
words_count = {}
for word in words:
    if word in words_count:
        words_count[word] += 1
        print(words_count)
    else:
        words_count[word] = 1
for word, count in words_count.items():
    print(word, ":", count)
#3
rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}
currency = input('Vyberit valyutu: ')
suma = float(input('Vvedit sumu(u hryvnyah): '))
if currency in rates:
    suma2 = suma / rates[currency]
    print('Suma in', currency, '=', suma2)
else: 
    print('Nevidoma valyuta')
#4
dictionary = {
    'hello': 'Привіт',
    'goodbye':'Допобачення',
    'teacher':'Вчитель',
    'student':'Студент',
    'grade':'Оцінка'
}
word = input('Vvedit slovo, yake bazhaete pereklasty: ').lower()
if word in dictionary:
    print('Pereklad:', dictionary[word])
else:
    print('Slovo ne znaydeno')
