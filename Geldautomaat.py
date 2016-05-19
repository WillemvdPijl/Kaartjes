Automaat = "Aan"
OpnameLimiet = 1500
Voorraad = 1000
Saldo = 25000

def Run():
    print("Welkom bij ING")
    print("Uw saldo bedraagt momenteel: €" + str(Saldo)"...")
    o = int(input("Hoeveel geld wilt u opnemen?"))

    if o < 0:
        print("Aanvraag mag niet negatief zijn, probeer opnieuw...\n")
        Run()
    elif (Saldo - o) < 0:
        print("Saldo niet toereikend... Ga geld verdienen man, skeere tata!\n")
        Run()
    elif

if Automaat == "Uit":
    print("Buiten bedrijf...")
elif Automaat == "Aan":
    Run()
