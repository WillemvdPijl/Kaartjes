def Main():
    t = input("Online of bij de kassa? Type 'o' voor online 'k' voor kassa: ")

    def Kassa():
        e = input("Is er iemand met een abonnement? Type dan met kleine letters 'ja' of 'nee'")
        a = int(input("Hoeveel volwassenen? v.a. 13 jaar. (Gehandicapten begeleiders vallen hier niet onder): "))
        b = int(input("Hoeveel kidnderen? 3 t/m 12 jaar: "))
        c = int(input("Hoeveel baby's en/of peuters? 0 t/m 2 jaar: "))
        d = int(input("Hoeveel begeleiders (vanaf 13 jaar) van gehandicapte personen (vanaf 3 jaar): "))

        #bij foute invoer
        if a < 0 or b < 0 or c < 0 or d < 0:
            print("Aantal kaartjes mag niet negatief zijn, probeer het opnieuw...\n")
            Kassa()
        if e != "ja" or e != "nee":
            print("Type 'ja' of 'nee' in kleine letters a.u.b.")
            Kassa()

        BT = (a + b + d)  #Betaalde tickets
        k = (a + b + c + d)  #Aantal tickets
        if t == "o" or t == "O":
            p = (a * 20 + b * 15.50 + d * 12)  #totale prijs
        elif t == "k" or t == "K":
            p = (a * 22 + b * 17.50 + d * 12)  #totale prijs

        #groepskorting
        korting = 2 * BT
        if k > 19:
            p = p - korting
        if (a + b + c) <= 4 and e == "ja":
            BT = (BT + (p * 0.25))
            p = p * 0.75

        #Print resultaten
        print( )
        print("-Aantal tickets " + str(k))
        print("-Totale prijs: €" + str(p))
        if k > 19:
            print("-Korting: €" + str(BT))

    #bij foute invoer
    if t == "o" or t == "k" or t == "O" or t == "K":
        Kassa()
    elif t != "o" and t != "k":
        print("Type 'o' voor online kaarten of 'k' voor kassa kaarten a.u.b.\n")
        Main()
Main()