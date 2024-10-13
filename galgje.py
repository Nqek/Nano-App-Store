import random

def galgje():
    with open("galgje.txt", "r") as infile:
        lines =  infile.readlines()

    makkelijk = []
    gemiddeld = []
    moeilijk = []

    moeilijkheid = None
    for line in lines:
        line = line.strip()
        if line == "# makkelijk":
            moeilijkheid = "makkelijk"
        elif line == "# gemiddeld":
            moeilijkheid = "gemiddeld"
        elif line == "# moeilijk":
            moeilijkheid = "moeilijk"
        elif line:
            if moeilijkheid == "makkelijk":
                makkelijk.append(line)
            elif moeilijkheid == "gemiddeld":
                gemiddeld.append(line)
            elif moeilijkheid == "moeilijk":
                moeilijk.append(line)
    keuze = input("Kies een moeilijkheid. Kies 1 voor makkelijk, 2 voor gemiddeld en 3 voor moeilijk. ")

    if keuze == "1":
        woordenlijst = makkelijk
        print("Je hebt voor makkelijk gekozen.")
    elif keuze == "2":
        woordenlijst = gemiddeld
        print("Je hebt voor gemiddeld gekozen.")
    elif keuze == "3":
        woordenlijst = moeilijk
        print("Je hebt voor moeilijk gekozen.")
    else:
        print("Deze keuze is niet mogelijk. Je mag een woord raden van de makkelijke graad.")
        woordenlijst = makkelijk

    geheim_woord = random.choice(woordenlijst).strip()
    geraden_letters = ""

    while True:
        aantal_gokken = input(f"Het woord heeft {len(geheim_woord)} letters. Hoeveel kansen om te raden wil je hebben? ")

        if aantal_gokken.isdigit():
            aantal_gokken = int(aantal_gokken)
            break
        else:
            print("Voer een geldig nummer in, je kan geen letters of tekens invoeren.")

    while aantal_gokken > 0:
        gok = input("Voer een letter in: ")
        if gok in geraden_letters:
            print(f"Je hebt de letter {gok} al geraden. Probeer een nieuwe letter.")
            continue

        if gok in geheim_woord:
            print(f"Ja! De letter {gok} zit in het geheime woord. ")
        else:
            aantal_gokken -= 1
            print(f"Nee. De letter {gok} zit niet in het geheime woord. Je hebt nog {aantal_gokken} poging(en) over.")

        geraden_letters += gok
        foute_letters = 0

        for letter in geheim_woord:
            if letter in geraden_letters:
                print(f"{letter}", end="")
            else:
                print("_", end="")
                foute_letters += 1
        print("")

        if foute_letters == 0:
            print(f"Goedzo! Je hebt het geheime woord geraden! Het woord was {geheim_woord}.")
            break

    else:
        print(f"Helaas. Je hebt het geheime woord niet geraden. Het woord was {geheim_woord}. ")
if __name__ == "__main__":
    galgje()