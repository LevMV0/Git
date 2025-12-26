numbers_sum= 10+5
print (numbers_sum)
numbers_mult = numbers_sum * 10
print (numbers_mult)
numbers_sum = 12+100
print (numbers_sum)
#del numbers_sum
#print (numbers_sum)
#numbers_sum is not defined
user_name = None
print (type(numbers_sum))
#число в назві змінної може бути в кінці, в середині, але не на початку
#ніяких спеціальних значень, крім "_" у назві перемінної
#коніенції(узгодження) в назві змінних з двох слів:
classWork = 1
#camelCase - перше слово з маленької літери, друге - з великої
ClassWork = 2
#PascalCase - кожне слово починається з великої літери
class_work = 3
#snake|_case - слова розділені "_"
#всі вони будуть прийматися різними
number = 20
print(number)
#number = number + 5
number += 5
print (number)
number -= 5
print (number)
number *= 5
print (number)
number /= 5
print (number)
number %= 5
print (number)
number //= 5
print (number)
number **= 5
print(number)
user_name = "Maria"
user_age = 16
print (f"Hello, {user_name}")
print(f"Your age is {user_age}")
print (f"5+10={5+10}")
user_name = input("Enter your name")
user_age = input("Enter your age")
#розробити програму, яка приймає від користувача числа від 2 і виводить їх добуток
num1 = float(input ("Введіть перше число:"))
num2 = float(input("Введіть друге число:"))
#float(input()) надання типу float
def new_func(num1, num2):
    print(type(num1))
    print(type(num2))
    num1 = int(num1)
#перетворення значень
    num2 = float(num2)
    print(type(num1))
    print(type(num2))
    return num1,num2

num1, num2 = new_func(num1, num2)
print (f"{num1}*{num2} = {num1*num2}")