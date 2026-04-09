import random

devinette = random.randint(1, 100)

def niveau():
    print(f"Veuillez Choisir le niveau: Facile, Normal, Difficile")
    choix = input("Votre choix est: ")
    

    if choix == "Facile":
        devinette = random.randint(1, 10)
        print("Vous avez choisi le niveau facile, vous devez deviner un nombre entre 1 et 10")
        print(jeux_devinette())

    elif choix == "Normal":
        devinette = random.randint(1, 50)
        print("Vous avez choisi le niveau normal, vous devez deviner un nombre entre 1 et 50")
        print(jeux_devinette())

    elif choix == "Difficile":
        devinette = random.randint(1, 100)
        print("Vous avez choisi le niveau difficile, vous devez deviner un nombre entre 1 et 100")
        print(jeux_devinette())

niveau()


def jeux_devinette():

    tries = 0
    max_tries = 3
    while tries < max_tries:
        number = (int(input("entrez un chiffre: ")))
        again = max_tries - tries - 1
        if number > devinette:
            print(f"pas de chance trop grand essaie, il vous reste encore {again} essaie")
        elif number < devinette:
            print(f"pas de chance trop petit essaie encore, il vous reste encore {again} essaie")
        elif number == devinette:
            print(f"you did it cogratulation the number was {devinette}")
            break
        tries += 1
    print(f"Oups vous avez perdu, la reponse etait {devinette}")
    if abs(number - devinette) <= 1:
        print("vous etes tres proche")
    elif abs(number - devinette) >= 3:
        print("vous etes proche")
    elif abs(number - devinette) > 5:
        print("vous etes loin")

    jeux_devinette()

def rejouer():
    print(f"Voulez-vous rejouer? Oui/Non")
    answer = input("Votre choix est:")
    if answer == "Oui":
        print(niveau())
    elif answer == "Non":    
        print("Merci d'avoir joué, à bientôt!")
    rejouer()