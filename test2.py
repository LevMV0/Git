text = input("Vvedit text: ")
words = text.split()
for i in range(len(words) -1, -1, -1):
    print(words[i], end=" ")