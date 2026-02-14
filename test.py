text = input("Vvedit text: ")
slovo1 = "привіт" 
slovo2 = "пока" 
slovo3 = "світ"
text1 = text.replace(slovo1,slovo1.upper())
text2 = text1.replace(slovo2, slovo2.upper())
text3 = text2.replace(slovo3, slovo3.upper())
print(text3)