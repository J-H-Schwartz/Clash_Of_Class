from characters import Warrior, Wizard


def main():
    height1 = 0
    weight1 = 0
    height2 = 0
    weight2 = 0

    nom1 = input("Entrez un nom: ")
    personnage1 = Wizard(nom1)
    while not 169 < height1 < 191:
        height1 = int(input("Entrez une taille entre 170 et 190 cm: "))
    personnage1.height = height1
    while not 69 < weight1 < 91:
        weight1 = int(input("Entrez un poids entre 70 et 90kg: "))
    personnage1.weight = weight1
    print(personnage1)

    nom2 = input("Entrez un nom: ")
    personnage2 = Warrior(nom2)
    while not 169 < height2 < 191:
        height2 = int(input("Entrez une taille entre 170 et 190 cm: "))
    personnage2.height = height2
    while not 69 < weight2 < 91:
        weight2 = int(input("Entrez un poids entre 70 et 90kg: "))
    personnage2.weight = weight2
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
