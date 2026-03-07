#1
def quote():
    print("\"Don't let others' opinions" 
        "\n\t drown your own inner voice.\""
        "\n\t\t Steve Jobs")
quote()
#2
def odd_nums(first, second):
    if first > second:
        first, second = second, first
    for num in range (first, second):
        if num % 2 != 0:
            print(num, end = ', ')
    print()
first = int(input('Vvedit pershe chyslo: '))
second = int(input('Vvedit druge chyslo: '))
odd_nums(first, second)
#3
def line(l, d, s):
    if d == 'h':
        print(s * l)
    elif d == 'v':
        for _ in range(l):
            print(s)
    else:
        print('error')
l = int(input('Vvedit dovzhynu: '))
d = input('Vvedit napryamok: ')
s = input('Vvedit symvol: ')
line(l, d, s)
#4
def numbers(num1, num2, num3, num4):
    return max(num1, num2, num3, num4)
num1 = int(input('Vvedit pershe chyslo: '))
num2 = int(input('Vvedit druge chyslo: '))
num3 = int(input('Vvedit trete chyslo: '))
num4 = int(input('Vvedit chetverte chyslo: '))
result = numbers(num1, num2, num3, num4)
print(result)
#5
def proste(num):
    if num <= 1:
        return False
    for n in range(2, num):
        if num % n == 0:
            return False
    return True
num = int(input('Vvedit chyslo: '))
if proste(num) == True:
    print(num)
#6
def happy(num):
    if num < 100000 or num > 999999:
        return False
    a = num // 100000 % 10
    b = num // 10000 % 10
    c = num // 1000 % 10
    d = num // 100 % 10
    e = num // 10 % 10
    f = num % 10
    return a + b + c == d + e + f
num = int(input("Vvedit 6-znachne chyslo: "))
if happy(num) == True:
    print(num)