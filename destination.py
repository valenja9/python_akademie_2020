MESTA = ('Prague', 'Wien','Brno','Svitavy','Zlin','Ostrava')  #ulozeni do promene
CENA = (150, 200, 120, 120, 100, 180) #kontejner
ODDELOVAC = 40*'='
UVITANI = 'Vitejte u nasi aplikace Destinatio!'

print(ODDELOVAC)
print(UVITANI)
print(ODDELOVAC)
print('''
1 - Praha   | 150 
2 - Viden   | 200
3 - Brno    | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
''')
print(ODDELOVAC)
cilova_destinace = input("Zadej jmeno lokality: ")
cilova_destinace_index = float(input("Zadej nejake cislo: "))
JMENO = input("Zadej jmeno: ")
PRIJMENI = input('Zadej prijmeni: ')
VEK = input('Zadej vek: ')
EMAIL = input('Zadej svuj email: ')
HESLO = input('Zadej svoje heslo: ')
print(ODDELOVAC)

index_lokality = MESTA.index(cilova_destinace)
cena_cilove_destinace = CENA[index_lokality]

print("UZIVATEL: ", JMENO)
print("DESTINACE: " + cilova_destinace)
print(f'CENA(cil:{cilova_destinace}): ', cena_cilove_destinace)
print('Jizdenku posleme na Vasi emailovou adresu: ', EMAIL)

