# print("Hello, Igor!")
# print(10)
# print(10 + 7)
needed_potatoes = int(input("Skilky kartopli pochystyty? "))
peeled_potatoes = 0
# print("Beremo kartoplu")
# print("Chystymo kartoplu")
# print("Gotovo")
# peeled_potatoes +=1
# print("Beremo kartoplu")
# print("Chystymo kartoplu")
# print("Gotovo")
# peeled_potatoes +=1
# print("Beremo kartoplu")
# print("Chystymo kartoplu")
# print("Gotovo")
# peeled_potatoes +=1
# print("Beremo kartoplu")
# print("Chystymo kartoplu")
# print("Gotovo")
# peeled_potatoes +=1
# print(f'Pochystyly {peeled_potatoes} kartopli!')
while peeled_potatoes < needed_potatoes:
    print("Beremo kartoplu")
    is_rotten = input('Kartoplya gnyla?')
    if rotten == 'tak':
        print('Vykydaemo')
        continue
    print(f"Chystymo kartoplu... Pochystyly {peeled_potatoes} kartopli!")
    print("Gotovo!")
    peeled_potatoes +=1
    is_tired = input('Vy vtomylys?')
    if is_tired == 'tak':
        break
    else:
        print('Pochystyly vsu kartoplu')
print(f'Pochystyly {peeled_potatoes} kartopli!')



# num1 = float(input('Vvedit pershe chyslo: '))
# num2 = float(input('Vvedit druge chyslo: '))
# action = input('Vvedit operaziu(+, -, *, /): ')
# match action:
#     case '+': print(f'{num1} + {num2} = {num1 + num2}')
#     case '-': print(f'{num1} - {num2} = {num1 - num2}')
#     case '*': print(f'{num1} * {num2} = {num1 * num2}')
#     case '/':
#         if num2 == 0: print('Nemozhna dilyty na null')
#         else: print(f'{num1} / {num2} = {num1 / num2}')
#     case _: print('Nekorektna operaziya')
# q = input('Input \'q\' to quit or pres Enter to continue')
# if q == 'q':
#     break