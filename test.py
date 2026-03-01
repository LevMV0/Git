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

