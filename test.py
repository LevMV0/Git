word1 = input('Vvedit pershe slovo: ').lower()
word2 = input('Vvedit druge slovo: ').lower()
if set(word1) == set(word2):
    print('Slova mayut odnakovi mnozhyny bukv')
else:
    print('Slova ne mayut odnakovi mnozhyny bukv')