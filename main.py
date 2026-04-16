import random

#devinette = random.randint(1,100)

def niveau():
    print(f"Veuillez Choisir le niveau: Facile, Normal, Difficile")
    choix = input("Votre choix est: ").lower()

    while choix not in ["facile", "normal", "difficile"]:
        print("Choix invalide, veuillez choisir entre Facile, Normal ou Difficile.")
        choix = input("Votre choix est: ").lower()
    

    if choix == "facile":
        #devinette = random.randint(1, 10)
        print("Vous avez choisi le niveau facile, vous devez deviner un nombre entre 1 et 10")
        jeux_devinette(max_nombre=10)

    elif choix == "normal":
        #devinette = random.randint(1, 50)
        print("Vous avez choisi le niveau normal, vous devez deviner un nombre entre 1 et 50")
        jeux_devinette(max_nombre=50)

    elif choix == "difficile":
        #devinette = random.randint(1, 100)
        print("Vous avez choisi le niveau difficile, vous devez deviner un nombre entre 1 et 100")
        jeux_devinette(max_nombre=100)


def jeux_devinette(max_nombre):
    devinette = random.randint(1, max_nombre)
    tries = 0
    max_tries = 3
    while tries < max_tries:
        number = (input("entrez un chiffre: "))
        if number.isdigit():
                number = int(number)
        else:
            print("Veuillez entrer un nombre valide.")
            continue
        again = max_tries - tries - 1
        if number > devinette and tries < max_tries:
            print(f"pas de chance trop grand essaie encore")
        elif number < devinette and tries < max_tries:
            print(f"pas de chance trop petit essaie encore")
        elif number == devinette:
            print(f"you did it cogratulation the number was {devinette}")
            break
        tries += 1

        while again > 0:
            print(f"il vous reste {again} essais")
        else:
            print("Vous n'avez plus d'essais")

            difference = abs(number - devinette)
            
            if difference <= 1:
                print("vous etes tres proche")
            elif difference <= 5:
                print("vous etes proche")
            elif difference > 5:   
                print("vous etes loin")

    if tries == max_tries:
            print(f"Oups vous avez perdu, la reponse etait {devinette}")

niveau()

#print(f"Voulez-vous rejouer? Oui/Non")

#answer = input("Votre choix est:")

while True: 
    print(f"Voulez-vous rejouer? Oui/Non")
    answer = input("Votre choix est: ").lower()
   
    if answer != "oui":  
        print("Merci d'avoir joué, à bientôt!")
        break
    niveau()