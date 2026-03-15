#1
try:
    price = float(input('Input price: '))
    discount = float(input('Input discount: '))
    if discount > 100:
        raise Exception(discount)
    if discount > 1:
        discount = discount / 100
    print(f'Discounted price = {price - (price * discount)}')
except ValueError:
    print('Incorrect number!')
except Exception:
    print('Incorrect discount')
#2
try:
    dollars = float(input('Input amount of money: '))
    rate = float(input('Input euro currency rate: '))
    if dollars <= 0 or rate <= 0:
        raise Exception('Can not be less than 0 or equal to 0')
    print(f'Done! Amount of money in euro = {dollars / rate}')
except ValueError:
    print('Incorrect number!')
except ZeroDivisionError:
    print('Can\'t divide by zero!')
except Exception:
    print('The Amount of money and currency rate can not be less than zero or equal to zero!')
finally:
    print('Operation is done!')
        
#3
try:
    inp = input('Input your grades(sep by spaces): ')
    count = 0
    total = 0
    grades = inp.split()
    for grade in grades:
        grade = int(grade)
        if grade < 0 or grade > 100:
            raise Exception('Invalid grade')
        total += grade
        count += 1
    print(f'Mean = {total/count}')
except ValueError:
    print('Incorrect number!')
except ZeroDivisionError:
    print('Can\'t divide by zero!')
except Exception as g:
    print(f'Incorrect grade! {g}')
finally:
    print('Calculations completed!')
#4
try:
    balance = 10000
    amount = float(input('Enter the amount you want to withdraw: '))
    if amount % 10 != 0 or amount > balance:
        raise Exception('Invalid amount!')
except ValueError:
    print('Incorrect enter!')
except Exception:
    print(f'Invalid amount!')
finally:
    print('Transaction completed!')
#5
order = input("Enter your order number: ")
try:
    if not order.startswith("ORD") or not order[3:].isdigit():
        raise Exception("Invalid order number format!")  
except Exception:
    print("Invalid order number format!")
finally:
    print("Order checking is done!")
#6
data = input("Input your grades(sep by spaces): ")
numbers = []
total = 0
try:
    items = data.split()
    for item in items:
        try:
            num = float(item)
            numbers.append(num)
            total += num
        except ValueError:
            print(f"Warning: '{item}' is invalid.")
    try:
        average = total / len(numbers)
        print("Sum:", total)
        print("Average:", average)
    except ZeroDivisionError:
        print("No correct number.")
finally:
    print("Data processing complited.")
