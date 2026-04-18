import random

def obtenir_configuration_niveau():
    """Gere la selection du niveau de difficulte et retourne le nombre maximum a associer."""
    niveaux = {
        "facile": {"max": 10, "tentatives": 5},
        "normal": {"max": 50, "tentatives": 4},
        "difficile": {"max": 100, "tentatives": 3}
    }
    while True:
        choix = input(f"Choisissez votre niveau de difficulté ({', '.join(niveaux.keys())}): ").lower()
        if choix in niveaux:
            return choix , niveaux[choix]
        print("Choix invalide. Veuillez réessayer.")

def jouer_partie():
    """Logique d'une seule partie de devinette."""
    mon_niveau, config = obtenir_configuration_niveau()

    cible = random.randint(1, config["max"])
    tentatives_restantes = config["tentatives"]
    print(f"\nNiveau choisi: {mon_niveau.upper()}. Vous devez deviner un nombre entre 1 et {config['max']}.")

    while tentatives_restantes > 0:
        try:
            entree = input(f"[{tentatives_restantes} essais] Veuillez entree un nombre:")
            nombre = int(entree)
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre entier.")
            continue
        tentatives_restantes -= 1

        if nombre == cible:
            print(f"Bravo! le nombre etait bien {cible}. Vous avez gagné!")
            return {"victoire": True, "niveau": mon_niveau}
        
            #indice de distance
        if nombre > cible:
            print("c'est plus grand!")
        elif nombre < cible:
            print("c'est plus petit!")

    if tentatives_restantes == 0:

        print(f"Vous avez perdu! la reponse etait {cible}.")
        return {"victoire": False, "niveau": mon_niveau}
    
def main():
    """Point d'entrée du programme et gestion du palmares."""

    historique = []

    while True:
        resultat = jouer_partie()
        historique.append(resultat)

        #affichage du palmares rapide

        victoires = sum(1 for v in historique if v["victoire"])
        print(f"\n---- PALMARES : {victoires} victoire sur {len(historique)} parties ----")

        if input("\nRejouer? (oui/non): ").lower() != "oui":
            print("Merci d'avoir joué! À bientôt!")
            break
if __name__ == "__main__":    
    
    main()

    