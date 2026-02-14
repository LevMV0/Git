#1
text = input("Vvedit text: ")
count = text.count(".") + text.count("!") + text.count("?")
print(count)
#2
text = input("Введіть рядок: ")
reversed_text = ""
length = len(text)
for i in range(length -1, -1, -1):
    reversed_text += text[i]
if text == reversed_text:
    print("Text ye palindromom")
else:
    print("Text ne ye palindromom")
#3
text = input("Vvedit text: ")
slovo1 = "привіт" 
slovo2 = "пока" 
slovo3 = "світ"
text1 = text.replace(slovo1,slovo1.upper())
text2 = text1.replace(slovo2, slovo2.upper())
text3 = text2.replace(slovo3, slovo3.upper())
print(text3)
#4
text = input("Vvedit text: ")
symvol1 = input("Vvedit symvol1: ")
symvol2 = input("Vvedit symvol2: ")
text2 = text[text.index(symvol1):text.index(symvol2)+1]
print(text.replace(text2, ""))
#5
text = input("Vvedit text: ")
words = text.split()
symvoly = input("Vvedit nabir symvoliv: ")
for word in words:
    count = 0
    for symvol in symvoly:
        if symvol in word:
            count += 1
        else:
            print(word, end=' ')
#6
text = input("Vvedit text: ")
words = text.split()
for i in range(len(words) -1, -1, -1):
    print(words[i], end=" ")