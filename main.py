from characters import ElveWarrior, ElveWizard, ElveArcher, DwarfWarrior, DwarfWizard, DwarfArcher
import webbrowser


def main():
    while True:
        menu_jeu = input("(C)ommencer la partie / (L)exique des personnages").upper()
        if menu_jeu == "C":
            break
        elif menu_jeu == "L":
            while True:
                menu_lexique = input("Quel personnage souhaitez-vous consulter ?\n Dwarf Wizard (1) / Dwarf Archer (2)"
                                     " / Dwarf Warrior (3)\n Elve Wizard (4) / Elve Archer (5) / Elve Warrior (6)\n"
                                     " (Q)uitter").upper()
                if menu_lexique == "1":
                    webbrowser.open("./DwarfWizard.html")
                    continue
                elif menu_lexique == "2":
                    webbrowser.open("./DwarfArcher.html")
                    continue
                elif menu_lexique == "3":
                    webbrowser.open("./DwarfWarrior.html")
                    continue
                elif menu_lexique == "4":
                    webbrowser.open("./ElveWizard.html")
                    continue
                elif menu_lexique == "5":
                    webbrowser.open("./ElveArcher.html")
                    continue
                elif menu_lexique == "6":
                    webbrowser.open("./ElveWarrior.html")
                    continue
                elif menu_lexique == "Q":
                    print("Retour au menu précédent.")
                    break
                else:
                    print("Commande invalide, recommencez.")
            continue
        else:
            print("Commande Invalide, recommencez.")

    nom1 = input("Entrez un nom: ")
    while True:
        while True:
            race1 = input("Choisissez la race de votre personnage: (D)warf / (E)lve: ").upper()
            if race1 == "D":
                break
            elif race1 == "E":
                break
            else:
                print("Veuillez choisir une race valide.")
                continue
        while True:
            classe1 = input("Quelle classe voulez-vous jouer ? (W)izard / (A)rcher / Wa(R)rior: ").upper()
            if classe1 == "W":
                break
            elif classe1 == "A":
                break
            elif classe1 == "R":
                break
            else:
                print("Veuillez choisir une classe valide.")

        if race1 == "E" and classe1 == "W":
            choix1 = ElveWizard
            break
        elif race1 == "E" and classe1 == "A":
            choix1 = ElveArcher
            break
        elif race1 == "E" and classe1 == "R":
            choix1 = ElveWarrior
            break
        elif race1 == "D" and classe1 == "W":
            choix1 = DwarfWizard
            break
        elif race1 == "D" and classe1 == "A":
            choix1 = DwarfArcher
            break
        elif race1 == "D" and classe1 == "R":
            choix1 = DwarfWarrior
            break
        else:
            print("La configuration du personnage a échoué. Veuillez recommencer.")

    personnage1 = choix1(nom1)
    print(personnage1)

    nom2 = input("Entrez un nom: ")
    while True:
        while True:
            race2 = input("Choisissez la race de votre personnage: (D)warf / (E)lve: ").upper()
            if race2 == "D":
                break
            elif race2 == "E":
                break
            else:
                print("Veuillez choisir une race valide.")
                continue
        while True:
            classe2 = input("Quelle classe voulez-vous jouer ? (W)izard / (A)rcher / Wa(R)rior: ").upper()
            if classe2 == "W":
                break
            elif classe2 == "A":
                break
            elif classe2 == "R":
                break
            else:
                print("Veuillez choisir une classe valide.")

        if race2 == "E" and classe2 == "W":
            choix2 = ElveWizard
            break
        elif race2 == "E" and classe2 == "A":
            choix2 = ElveArcher
            break
        elif race2 == "E" and classe2 == "R":
            choix2 = ElveWarrior
            break
        elif race2 == "D" and classe2 == "W":
            choix2 = DwarfWizard
            break
        elif race2 == "D" and classe2 == "A":
            choix2 = DwarfArcher
            break
        elif race2 == "D" and classe2 == "R":
            choix2 = DwarfWarrior
            break
        else:
            print("La configuration du personnage a échoué. Veuillez recommencer.")

    personnage2 = choix2(nom2)
    print(personnage2)

    while True:
        inspection_personnage = input("Souhaitez vous voir la fiche de votre personnage ou débuter la partie ? {} "
                                      "(1) / {} (2) / (C)ommencer".format(personnage1.name, personnage2.name)).upper()
        if inspection_personnage == "1":
            personnage1.as_html()
            continue
        elif inspection_personnage == "2":
            personnage2.as_html()
            continue
        elif inspection_personnage == "C":
            break
        else:
            print("Commande invalide, recommencez.")

    personnage_actuel = personnage1
    personnage_oppose = personnage2
    print("")
    while personnage1.current_life > 0 and personnage2.current_life > 0:

        print("Au début de ce tour il reste {} points de vie à {}.".format(personnage_oppose.current_life,
                                                                           personnage_oppose.name))
        weapon, attack_points = personnage_actuel.attack()
        print(personnage_actuel.name + " frappe pour " + str(attack_points) + " points de dégats.")
        defence_points = personnage_oppose.defend(weapon, attack_points)
        print(personnage_oppose.name + " se défend pour pour " + str(defence_points) + " points de dégats.")
        damages_difference = attack_points - defence_points
        if damages_difference > 0:
            print("{} inflige {} points de dégats à {}.".format(personnage_actuel.name, damages_difference,
                                                                personnage_oppose.name))
        else:
            print("{} pare le coup porté par {}".format(personnage_oppose, personnage_actuel))
        print("Il reste " + str(personnage_oppose.current_life) + " points de vie à " + personnage_oppose.name + "\n")

        if personnage_actuel == personnage1:
            personnage_actuel = personnage2
            personnage_oppose = personnage1
        else:
            personnage_actuel = personnage1
            personnage_oppose = personnage2

    if personnage1.current_life == 0:
        print(personnage2.name + " gagne la partie.")
    if personnage2.current_life == 0:
        print(personnage1.name + " gagne la partie.")


if __name__ == "__main__":
    main()
