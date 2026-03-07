def happy(num):
    if num < 100000 or num > 999999:
        return False
    a = num // 100000 % 10
    b = num // 10000 % 10
    c = num // 1000 % 10
    d = num // 100 % 10
    e = num // 10 % 10
    f = num % 10
    return a * + b + c == d + e + f
num = int(input("Vvedit 6-znachne chyslo: "))
if happy(num) == True:
    print(num)
