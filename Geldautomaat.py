Automaat = "Aan"
OpnameLimiet = 1500
Voorraad = 1000
Saldo = 1000

def Run():
    print("Welkom bij ING")
    print("Uw saldo bedraagt momenteel: €" + str(Saldo) + ".")
    o = int(input("Hoeveel euro wilt u opnemen?: "))
    NSaldo = Saldo - o

    if o < 0:
        print("Aanvraag mag niet negatief zijn, probeer opnieuw...\n")
        Run()
    elif (Saldo - o) < 0:
        print("Saldo niet toereikend... Ga geld verdienen man, skeere tata!\n")
        Run()
    elif (Saldo - o) >= 0:
        print("U heeft €" + str(o) + " opgenomen. Uw saldo bedraagt momenteel: €" + str(NSaldo) + ".")
        print("Bedankt voor het gebruiken van ING, nog een fijne dag\n")
        Run()
    elif (OpnameLimiet - o) < 0:
        print("Dagelijkse opnamelimiet wordt overschreden, probeer opnieuw\n")
        Run()
    elif (Voorraad - o) < 0:
        print("Biljetten voorraad niet toerekend, probeer opnieuw...\n")
        Run()

if Automaat == "Uit":
    print("Buiten bedrijf...")
elif Automaat == "Aan":
    Run()
