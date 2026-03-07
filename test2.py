def palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]
num = int(input("Vvedit chyslo: "))
if palindrome(num) == True:
    print(num)
