A = int(input("Vvedit chyslo: "))
N = int(input("Vvedit stupin: "))
A2 = A
if N == 0:
    A2 = 1
    print(A2)
elif N > 0:
    stupin = 1
    while stupin != N:
        stupin += 1
        A2 *= A 
    print (A2)
elif N < 0 and A != 0:
    stupin = 1
    while stupin != -N:
        stupin += 1
        A2 *= A 
    print (1/A2)
elif N < 0 and A == 0:
    print("error")