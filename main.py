from characters import Warrior, Wizard


def main():
    nom1 = input("Entrez un nom: ")
    personnage1 = Wizard(nom1)
    print(personnage1)
    nom2 = input("Entrez un nom: ")
    personnage2 = Warrior(nom2)
    print(personnage2)
    personnage_actuel = personnage1
    personnage_oppose = personnage2
    print("")
    while personnage1.current_life > 0 and personnage2.current_life > 0:
        print("Au début de ce tour il reste {} points de vie à {}.".format(personnage_oppose.current_life,
                                                                           personnage_oppose.nom))
        weapon, attack_points = personnage_actuel.attack()
        print(personnage_actuel.nom + " frappe pour " + str(attack_points) + " points de dégats.")
        defence_points = personnage_oppose.defend(weapon, attack_points)
        print(personnage_oppose.nom + " se défend pour pour " + str(defence_points) + " points de dégats.")
        damages_difference = attack_points - defence_points
        if damages_difference > 0:
            print("{} inflige {} points de dégats à {}.".format(personnage_actuel.nom, damages_difference,
                                                                personnage_oppose.nom))
        else:
            print("{} pare le coup porté par {}".format(personnage_oppose, personnage_actuel))
        print("Il reste " + str(personnage_oppose.current_life) + " points de vie à " + personnage_oppose.nom + "\n")

        if personnage_actuel == personnage1:
            personnage_actuel = personnage2
            personnage_oppose = personnage1
        else:
            personnage_actuel = personnage1
            personnage_oppose = personnage2

    if personnage1.current_life <= 0:
        print(personnage2.nom + " gagne la partie.")
    if personnage2.current_life <= 0:
        print(personnage1.nom + " gagne la partie.")


if __name__ == "__main__":
    main()
