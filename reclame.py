from algemene_functies import mijn_functie_2


def aanbieding_1(smaak, prijs, korting):
    korting = prijs - korting * prijs 
    uitvoer = f"Vandaag in de aanbieding: emmertje ijs (1 liter) in de smaak {smaak}, van {prijs} euro voor {korting:.2f} euro."
    print(uitvoer)

def inkomsten_totaal(inkomsten,btw):
    totaal = 0
    for i in inkomsten:
        totaal = totaal + i 
    bedrag = totaal * btw
    print(f"Het totaal van alle inkomsten deze week is {totaal} euro, waarover {bedrag} euro btw betaald dient te worden.")

def laag_en_hoog(mijn_lijst):
    print(max(mijn_lijst),min(mijn_lijst))

def gemiddelde(mijn_lijst):
    average = sum(mijn_lijst) / len(mijn_lijst)
    print(f"De gemiddelde inkomsten deze week zijn {average} euro.")
    
def meervoudig(invoer_lijst):
    return laag_en_hoog(invoer_lijst)

def combinatie(invoer_lijst_2):
    korte_lijst = laag_en_hoog(invoer_lijst_2)
    uitvoer = mijn_functie_2(korte_lijst[0],korte_lijst[1])
    return uitvoer