#1
text = input("Vvedit text: ")
print(len(text))
#2
text = input("Vvedit text: ")
symvol = input("Vvedit symvol: ")
count = 0
for i in text:
    if i == symvol:
        count += 1
print(count)
#3
text = input("Введіть рядок: ")
reversed_text = ""
length = len(text)
for i in range(length -1, -1, -1):
    reversed_text += text[i]
print(reversed_text)
#4
text = input("Vvedit text: ")
slovo = input("Vvedit slovo: ")
count = text.count(slovo)
print(count)
#5
text = input("Vvedit text: ")
slovo_poshuku = input("Vvedit slovo poshuku: ")
slovo_zaminy1 = input("Vvedit slovo zaminy: ")
slovo_zaminy2 = input("Vvedit slovo dlya zaminy: ")
count = text.count(slovo_poshuku)
print(count)
zminenyi_text = text.replace(slovo_zaminy2, slovo_zaminy1)
print(zminenyi_text)
#6
text = input("Vvedit text: ")
words = text.split()
longest_word = words[0]
for word in words:
    if len(word) > len(longest_word):
        longest_word = word
print(longest_word)