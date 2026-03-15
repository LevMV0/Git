#my_list = ['orange', 'apole', 'banana']
#print(my_list[10]) error
# def recurtion():
#     recurtion() error
# print(10/0) error
operators = [ '+', '-', '*', '/']
while True:
    try:
        num1 = float(input())
        num2 = float(input())
        action = input("(+, -, *, /): ")
        if action not in operators:
            raise Exception(action)
            #raise Exception
        match action:
            case '+': print(f'{num1} + {num2} = {num1 + num2}')
            case '-': print(f'{num1} - {num2} = {num1 - num2}')
            case '*': print(f'{num1} * {num2} = {num1 * num2}')
            case '/': print(f'{num1} / {num2} = {num1 / num2}')
    except ValueError:
        print('Incorrect number!')
    except ZeroDivisionError:
        print('Can\'t divide by zero!')
    #except Exception:
        #print('Incorrect operation!')
    except Exception as ex:
        print(f'Incorrect operation! {ex.args[0]}')
    finally:
        repeat = input('Do you want to repeat? ')
        if repeat.lower() == 'n':
            break