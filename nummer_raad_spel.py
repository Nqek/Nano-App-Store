import random

def Raad():
    while True:
        getal1 = input("Je kunt zelf kiezen tussen welk getal je kunt kiezen. het laagste getal blijft 1. Wat wil je als hoogste getal? ")
        if getal1.isdigit():
            getal1 = int(getal1)
            if getal1 > 1:
                break
            else:
                print("Het getal moet hoger zijn dan 1. Probeer opnieuw.")
        else:
            print("Voer een geldig positief nummer in.")

    while True:
        poging = input("Hoeveel pogingen denk je nodig te hebben om het juiste nummer te raden? ")
        if poging.isdigit():
            poging = int(poging)
            break
        else:
            print("Voer een geldig nummer in.")
    print(f"Je hebt {poging} pogingen om het juiste getal tussen de 1 en {getal1} te raden.")

    random_getal = random.randint(1, getal1)

    for i in range(poging):
        goed_getal = int(input(f"Poging {i + 1}: Voer je nummer in: "))

        if goed_getal < random_getal:
            print("Fout, je zit te laag.")

        elif goed_getal > random_getal:
            print("Fout, je zit te hoog.")

        else:
            print("Je hebt het goede nummer geraden!")
            break

    else:
        print(f"Helaas je hebt het juiste antwoord niet geraden. Het goede getal was {random_getal}")

if __name__ == "__main__":
    Raad()
