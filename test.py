numbers_input = input("Vvedit spysok chysel: ")
n = int(input("Vvedit kilkist pozytsii N: "))
numbers = [int(x) for x in numbers_input.split(', ')]
shifted = numbers[-n:] + numbers[:-n]
print(shifted)