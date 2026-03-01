#1
dictionary = {
    'hello': 'Привіт',
    'goodbye':'Допобачення',
    'teacher':'Вчитель',
    'student':'Студент',
    'grade':'Оцінка'
}
word = input('Vvedit slovo, yake bazhaete pereklasty: ').lower()
if word in dictionary:
    print('Pereklad:', dictionary[word])
else:
    print('Slovo ne znaydeno')
#2
kilkist = int(input('Vvedit kilkist druziv: '))
my_games = set(input('Vvedit vashui igry: ').lower().split(', '))
count = 0
druzi = []
for count in range(kilkist):
    drug = input('Vvedit im\'ya druga: ')
    if drug not in druzi:
        druzi.append(drug)
    fr_games = set(input('Vvedit igry druga: ').lower().split(', '))
    spilni_igry = my_games & fr_games
print('Vy mozhete pograty razom u:', spilni_igry)