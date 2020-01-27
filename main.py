from characters import Warrior, Wizard, Archer


def main():

    nom1 = input("Entrez un nom: ")
    classe1 = input("Quelle classe voulez-vous jouer ? (W)izard / (A)rcher / Wa(R)rior: ").upper()
    if classe1 == "W":
        classe1 = Wizard
    elif classe1 == "A":
        classe1 = Archer
    elif classe1 == "R":
        classe1 = Warrior
    personnage1 = classe1(nom1)
    print(personnage1)

    nom2 = input("Entrez un nom: ")
    classe2 = input("Quelle classe voulez-vous jouer ? (W)izard / (A)rcher / Wa(R)rior: ").upper()
    if classe2 == "W":
        classe2 = Wizard
    elif classe2 == "A":
        classe2 = Archer
    elif classe2 == "R":
        classe2 = Warrior
    personnage2 = classe2(nom2)
    print(personnage2)

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

    if personnage1.current_life <= 0:
        print(personnage2.name + " gagne la partie.")
    if personnage2.current_life <= 0:
        print(personnage1.name + " gagne la partie.")


if __name__ == "__main__":
    main()
