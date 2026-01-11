# bool - True or False
'''
can_pinguins_swim = True
can_pinguins_fly = False
print(f"Can pinguins swim& {can_pinguins_swim}")
print (f"Can pinguins fly& {can_pinguins_fly}")
print (type (can_pinguins_swim))
print (type(can_pinguins_fly))

number = int(input("Vvedite chislo"))
print (f"{number} > 10? {number > 10}")
print (f"{number} < 10? {number < 10}")
print (f"{number} >= 10? {number >= 10}")
print (f"{number} <= 10? {number <= 10}")
print (f"{number} == 10? {number == 10}")
print (f"{number} != 10? {number != 10}")
'''
'''
is_raining = input("Is it raining outside?(yes/no) ")
if is_raining == "yes":
    print ("We need an umbrella")
else:
    print ("We do not need an umbrella")
is_cold = input ("Is it cold outside?(yes/no) ")
if is_cold == "yes":
    print ("We need to dress warmer")
else:
    print ("We do not need warmer clothing")

temperature = int(input("What temperature is it outside? "))
if temperature <= -10:
    print("Dress really warm!")
elif temperature > -10 and temperature <= 5:
    print("Dress warm")
elif temperature > 5 and <= 16:
    print(put on a jacket)
else:
    "Do not dress too warm"
print("Just go outside already!")

boolean = bool(0) #False
print(bool(0))
print(bool(0.0))
print(bool(''))
something = None
print(bool(something))
print(bool(10))
print(bool(-6.8))
print(bool('hello'))
'''
num1 = float(input("Vvedite pervoe chislo"))
num2 = float(input("Vvedite vtoroe chislo"))
operation = input("Vuberit operation(+,-,*,/)")
if operation == '+':
    print(f'{num1} + {num2} = {num1 + num2}')
elif operation == '-':
    print(f'{num1} - {num2} = {num1 - num2}')
elif operation == '*':
    print(f'{num1} * {num2} = {num1 * num2}')
elif operation == '/':
    if num2 == 0:
        print('Na nul ne mozhna dilutu!')
    else:
        print(f'{num1} / {num2} = {num1 / num2}')
else:
    print('Nekorektna operation!')