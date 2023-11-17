def lire_compteur():
    try:
        with open("data.txt", "r") as fichier:
            compteur = int(fichier.read())
            return compteur
    except FileNotFoundError:
        return 0  # Retourne 0 si le fichier n'existe pas

def incrementer_compteur():
    compteur = lire_compteur()
    compteur += 1

    with open("data.txt", "w") as fichier:
        fichier.write(str(compteur))

    with open("raison.txt", "w") as fichier_raison:
        fichier_raison.write("Entrer")

def decrementer_compteur():
    compteur = lire_compteur()
    
    if compteur > 0:
        compteur -= 1

        with open("data.txt", "w") as fichier:
            fichier.write(str(compteur))

        with open("raison.txt", "w") as fichier_raison:
            fichier_raison.write("Sortir")

def raison_inconnue():
    with open("raison.txt", "w") as fichier_raison:
        fichier_raison.write("Inconnue")

def modification_etat(new_value):
        with open("state.txt", "w") as fichier_etat:
            fichier_etat.write(str(new_value))
    
