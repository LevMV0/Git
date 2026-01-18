num = 123456
a = num % 10
b = num % 100
c = num % 1000
d = num % 10000
e = num % 100000
f = num % 1000000
print (f/100000)
a1 = a
b1 = (b - a)/10
c1 = (c - b)
d1 = (d - c)
e1 = (e - d)/10000
f1 = (f - e)/100000
if (f/100000) >= 1 and (f/100000) < 10:
    print(f'num2 = {a1 * 100000 + b1 * 10000 + c1 + d1 + e1 * 10 + f1}')
else:
    print("Error")