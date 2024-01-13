import os
import random

# Fonction pour nettoyer l'écran du terminal
def clear_screen():
    # Pour Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # Pour macOS et Linux
    else:
        _ = os.system('clear')

# Fonction pour afficher le plateau de jeu
def afficher_plateau(plateau):
    for i, ligne in enumerate(plateau):
        print(" | ".join(ligne))
        if i < 2:  # On ne dessine la ligne horizontale qu'après les deux premières lignes
            print("-"*9)

# Fonction pour vérifier s'il y a un gagnant
def verifier_gagnant(plateau, joueur):
    # Vérifier les lignes
    for ligne in plateau:
        if all([case == joueur for case in ligne]):
            return True

    # Vérifier les colonnes
    for col in range(3):
        if all([plateau[ligne][col] == joueur for ligne in range(3)]):
            return True

    # Vérifier les diagonales
    if all([plateau[i][i] == joueur for i in range(3)]) or all([plateau[i][2 - i] == joueur for i in range(3)]):
        return True

    return False

# Fonction pour trouver toutes les cases vides
def case_vide(plateau):
    return [(i, j) for i in range(3) for j in range(3) if plateau[i][j] == " "]

# Fonction pour le coup du bot
def coup_bot(plateau):
    cases_vides = case_vide(plateau)
    if cases_vides:
        i, j = random.choice(cases_vides)
        plateau[i][j] = "O"

# Fonction pour le coup du joueur
def coup_joueur(plateau):
    while True:
        try:
            entree = input("Entrez votre coup (ligne [1-3] colonne [1-3]): ")
            ligne, colonne = map(int, entree.split())
            ligne -= 1  # Ajuster pour l'index 0
            colonne -= 1
            if 0 <= ligne <= 2 and 0 <= colonne <= 2 and plateau[ligne][colonne] == " ":
                plateau[ligne][colonne] = "X"
                break
            else:
                print("Coup invalide. Essayez de nouveau.")
        except (ValueError, IndexError):
            print("Entrée invalide. Veuillez entrer le numéro de ligne et de colonne.")

# Initialisation du plateau de jeu
plateau = [[" " for _ in range(3)] for _ in range(3)]

# Début du jeu avec le joueur X
joueur_actuel = "X"

# Boucle principale du jeu
while True:
    clear_screen()  # Nettoie l'écran avant d'afficher le plateau
    afficher_plateau(plateau)
    
    if joueur_actuel == "X":
        coup_joueur(plateau)
    else:
        coup_bot(plateau)

    if verifier_gagnant(plateau, joueur_actuel):
        clear_screen()  # Nettoie l'écran avant d'afficher le plateau final
        afficher_plateau(plateau)  # Afficher le plateau final
        print(f"Le joueur {joueur_actuel} a gagné!")
        break

    if not case_vide(plateau):
        clear_screen()  # Nettoie l'écran avant d'afficher le plateau final
        afficher_plateau(plateau)  # Afficher le plateau final
        print("Match nul!")
        break

    joueur_actuel = "O" if joueur_actuel == "X" else "X"