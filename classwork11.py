def disc(prices: list):
    disc = []
    for price in prices:
        if price > 100:
            disc.append(price * 0.8)
    return disc
orig = [50, 120, 80, 200, 300]
result = disc(orig)
print(result)
def recursion():
    print('recursion')
    recursion()
def func_b():
    print('b calls a')
    func_a
def func_a():
    print('a calls b')
    func_b
#Factorial Loop
def fact(n):
    result = 1
    for i in range(1, n):
        result *= i
    return result
print(fact(5))

#Factorial Recurtion
def factR(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factR(n - 1)
print(factR(5))

def say():
    print('Hello')
func_var = say
def some_func(callback):
    print('some_func calls its callback')
    callback()
some_func(say)

#func_var() #operator vyklyku
#print(type(func_var))
def log_file(message):
    pass
def log_console(message):
    pass
def log_database(message):
    pass
def do_some_work(log_callback):
    print('Doing something...')
    print('Done!')
    log_callback('logging message')
do_some_work(log_database)
do_some_work(log_database)
do_some_work(log_file)


sum = lambda a, b: a + b
print(sum(10,12))
operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b
}
num1 = float(input())
num2 = float(input())
action = input()
if action in operations:
    print(operations[action](num1, num2))
else:
    print('Error')
    tax_rate = 0.2
def calculate_tax_impure(amount):
    return amount * tax_rate
print(calculate_tax_impure(10000))

def calculate_tax_pure(amount, tax_rate):
    return amount * tax_rate
print(calculate_tax_pure(10000, 0.3))

#cart impure
def add_pr(cart: list, product: str):
    cart.append(product)
    return cart
my_cart = ['apple', 'banana']
add_pr(my_cart, 'orange')
print(my_cart)

#cart pure
def add_pr(cart:list, product: list):
    new_cart = cart.copy()
    new_cart.append(product)
    return new_cart
my_cart = ['apple', 'banana']
add_pr(my_cart, 'orange')
print(my_cart)

my_set1 = {'apple', 'orange'}
my_set2 = {'pear', 'banana'}
union = my_set1.union(my_set2)
print(union)
number = [10, 5, 43, 8]
even_numbers = list()
