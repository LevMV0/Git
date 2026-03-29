#1
try:
    num1 = (input('Enter first number: '))
    num2 = (input('Enter second number: '))
    raise ValueError
    num1f = float(num1)
    num2f = float(num2)
except ValueError:
    print('Invalid number!')
except ZeroDivisionError:
    print('Can\'t divide by zero!') 
finally:
    print(f'Operation is done: {num1 / num2}')