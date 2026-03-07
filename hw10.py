#1
def quote():
    print("\"Don't compare yourself with anyone in this world..." 
        "\n\t if you do so, your insulting yourself.\""
        "\n\t\t Bill Gates")
quote()
#2
def even_nums(first, second):
    if first > second:
        first, second = second, first
    for num in range (first, second):
        if num % 2 == 0:
            print(num, end = ', ')
    print()
first = int(input('Vvedit pershe chyslo: '))
second = int(input('Vvedit druge chyslo: '))
even_nums(first, second)
#3
def sq(l, z, s):
    if z == "True":
        for _ in range(l):
            print(s * l)
    elif z == "False":
        for i in range(l):
            for j in range(l):
                if i == 0 or i == l - 1 or j == 0 or j == l - 1:
                    print(s, end=' ')
                else:
                    print(' ', end=' ')
            print()
    else:
        print('error')
l = int(input('Vvedit dovzhynu: '))
z = input('Vvedit logichnu zminnu(True or False): ')
s = input('Vvedit symvol: ')
sq(l, z, s)
#4
def number(num):
    num = abs(num)
    if num == 0:
        return 1
    count = 0
    while num > 0:
        num //= 10
        count += 1
    return count
num = int(input("Vvedit chyslo: "))
print(number(num))
#5
def palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
num = int(input("Vvedit chyslo: "))
if palindrome(num) == True:
    print(num)