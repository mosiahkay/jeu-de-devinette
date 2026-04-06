import random
print(f"Devine un nombre entre 1 et 20")
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
    print(f"you did it congratulation the number was {devinette}")
    break
  tries += 1
  if tries == max_tries:
    print(f"Oups vous avez perdu, la reponse etait {devinette}")
    break
  if abs(number - devinette) <= 2:
    print("vous etes tres proche")
  elif abs(number - devinette) >= 5:
    print("vous etes proche")