def Main():
    t = input("Online of bij de kassa? Type 'o' voor online 'k' voor kassa: ")

    def Kassa():
        a = int(input("Hoeveel volwassenen? v.a. 13 jaar. (Gehandicapten begeleiders vallen hier niet onder): "))
        b = int(input("Hoeveel kidnderen? 3 t/m 12 jaar: "))
        c = int(input("Hoeveel baby's en/of peuters? 0 t/m 2 jaar: "))
        d = int(input("Hoeveel begeleiders (vanaf 13 jaar) van gehandicapte personen (vanaf 3 jaar): "))

        BT = (a + b + d)  # Betaalde tickets
        k = (a + b + c + d)  # Aantal tickets
        if t == "o" or t == "O":
            p = (a * 20 + b * 15.50 + d * 12)  # totale prijs
        elif t == "k" or t == "K":
            p = (a * 22 + b * 17.50 + d * 12)  # totale prijs

        #groepskorting
        korting = 2 * BT
        if k > 19:
            p = p - korting

        #Print resultaten
        print( )
        print("Aantal tickets " + str(k))
        print("Totale prijs: €" + str(p))
        if k > 19:
            print("Korting: €" + str(BT))

    #bij foute invoer
    if t == "o" or t == "k" or t == "O" or t == "K":
        Kassa()
    elif t != "o" and t != "k":
        print("Type 'o' voor online kaarten of 'k' voor kassa kaarten a.u.b.")
        Main()
Main()