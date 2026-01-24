#1
num = float(input("Введіть число: "))
stepen = int(input("Оберіть бажану степінь(0-7): "))
match stepen:
    case 0: 
        print(f'{num ** 0}')
    case 1: 
        print(f'{num ** 1}')
    case 2: 
        print(f'{num ** 2}')
    case 3: 
        print(f'{num ** 3}')
    case 4: 
        print(f'{num ** 4}')
    case 5: 
        print(f'{num ** 5}')
    case 6: 
        print(f'{num ** 6}')
    case 7: 
        print(f'{num ** 7}')
#2
num = float(input("Введіть число(1-100): "))
match num:
    case _ if num % 3 == 0 and num % 5 == 0 and num / 100 >= 1/100 and num/100 <= 1: print("Fizz Buzz")
    case _ if num % 3 == 0 and num / 100 >= 1/100 and num/100 <= 1: print("Fizz")
    case _ if num % 5 == 0 and num / 100 >= 1/100 and num/100 <= 1: print("Buzz")
    case _ if num % 3 != 0 and num % 5 != 0 and num / 100 >= 1/100 and num/100 <= 1: print(num)
    case _:
        print("Error")
#3
zak = (input("Oberit zakusku(salat, sup, no): ")) #- no zakuska
osnstr = (input("Oberit osn str(kurka, ryba, no): "))
desert = (input("Oberit desert(morozyvo, fructy, no): "))
status = (input("Vvedit vash statys(gist, postiyniy client): "))
total = 0 #startoviy check
Znyzhka = 0 #startova znyzhka
match zak:
    case "salat":
        total = total + 5
    case "sup":
        total = total + 7
match osnstr:
    case "kurka":
        total = total + 10
    case "ryba":
        total = total + 12
match desert:
    case "morozyvo":
        total = total + 3
    case "fructy":
        total = total + 4
if zak != "no" and osnstr != "no" and desert != "no":
        Znyzhka = Znyzhka + (total * 0.10)
if total > 20:
        Znyzhka = Znyzhka + (total * 0.15)
if status == "postiyniy client":
        Znyzhka = Znyzhka + (total * 0.05)
if zak == "salat" and osnstr == "ryba" and desert != "no":
        total = total - 2
if osnstr == "kurka" and desert == "morozyvo":
        print("Beskoshtovniy napiy u podarunok!")
total = total - Znyzhka
print(total)