import random

def niveau():
    print(f"Veuillez Choisir le niveau: Facile, Normal, Difficile")
    choix = input("Votre choix est: ")

    if choix == "Facile":

        print(f"Devine un nombre entre 1 et 10")
        def jeux_devinette():
            devinette = (int(random.randint(1,10)))
            tries = 0
            max_tries = 3
            while tries < max_tries:
                number = (int(input("entrez un chiffre: ")))
                again = max_tries - tries - 1
                if number > devinette:
                    print(f"pas de chance trop grand essaie, il vous reste encore {again} essaie")
                elif number < devinette:
                    print(f"pas de chance trop petit essaie encore, il vous reste encore {again} essaie")
                else:
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
            return
        print(jeux_devinette())

    elif choix == "Normal":
        print(f"Devine un nombre entre 1 et 20")
        def jeux_devinette():
            devinette = (int(random.randint(1,20)))
            tries = 0
            max_tries = 3
            while tries < max_tries:
                number = (int(input("entrez un chiffre: ")))
                again = max_tries - tries - 1
                if number > devinette:
                    print(f"pas de chance trop grand essaie, il vous reste encore {again} essaie")
                elif number < devinette:
                    print(f"pas de chance trop petit essaie encore, il vous reste encore {again} essaie")
                else:
                    print(f"you did it cogratulation the number was {devinette}")
                    break
                tries += 1
            print(f"Oups vous avez perdu, la reponse etait {devinette}")
            if abs(number - devinette) <= 2:
                print("vous etes tres proche")
            elif abs(number - devinette) >= 5:
                print("vous etes proche")
            elif abs(number - devinette) > 10:
                print("vous etes loin")
            return
        print(jeux_devinette())
            
    elif choix == "Difficile":
        print(f"Devine un nombre entre 1 et 50")
        def jeux_devinette():
            devinette = (int(random.randint(1,50)))
            tries = 0
            max_tries = 3
            while tries < max_tries:
                number = (int(input("entrez un chiffre: ")))
                again = max_tries - tries - 1
                if number > devinette:
                    print(f"pas de chance trop grand essaie, il vous reste encore {again} essaie")
                elif number < devinette:
                    print(f"pas de chance trop petit essaie encore, il vous reste encore {again} essaie")
                else:
                    print(f"you did it cogratulation the number was {devinette}")
                    break
                tries += 1
            print(f"Oups vous avez perdu, la reponse etait {devinette}")
            if abs(number - devinette) <= 5:
                print("vous etes tres proche")
            elif abs(number - devinette) >= 10:
                print("vous etes proche")
            elif abs(number - devinette) > 15:
                print("vous etes loin")
            return
        print(jeux_devinette())

    return
print(niveau())

print(f"Voulez-vous rejouer? Oui/Non")
answer = input("Votre choix est:")
if answer == "Oui":
    print(niveau())
elif answer == "Non":    
    print("Merci d'avoir joué, à bientôt!")