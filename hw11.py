#1
def nsd(a, b):
    if b == 0:
        return a
    return nsd(b, a % b)
a = int(input("VVedit pershe chyslo: "))
b = int(input("Vvedit druge chyslo: "))
print("НСД =", nsd(a, b))
#2
def suma(n):
    if n == 0:
        return 0
    return n % 10 + suma(n // 10)
num = int(input("Vedit chyslo: "))
print("Suma:", suma(num))
#3
def is_symmetric(lst):
    if len(lst) <= 1:
        return True
    if lst[0] != lst[-1]:
        return False
    return is_symmetric(lst[1:-1])
numbers = []
numbers_input = (input("Vvedit chysla(cherez probil)"))
numbers_splited = numbers_input.split()
for number in numbers_splited:
    numbers.append(number)
if is_symmetric(numbers):
    print("Spysok symetrichnyi")
else:
    print("Spysok ne symetrichnyi")