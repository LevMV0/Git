figura = input("Oberit figuru(kvadrat abo praymokutnyk): ")
symvol = input("Oberit symvol: ")
if figura == 'kv':
    storona = int(input("Vvedit dovzhynu storony: "))
    for i in range(storona):
        print(symvol * storona)
elif figura == 'pr':
    shyryna = int(input("Vvedit shyrynu: "))
    vysota = int(input("Vvedit vysoty: "))
    for i in range(vysota):
       print(symvol * shyryna)
        