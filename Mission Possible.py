import galgje
import nummer_raad_spel

print("1. Nummer raad spel")
print("2. Galgje")

keuze = input("Welk spel wil je spelen? ")
if keuze == "1":
    nummer_raad_spel.Raad()
if keuze == "2":
    galgje.galgje()
else:
    print("Deze waarde is niet geldig. Probeer het opnieuw.")
