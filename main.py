from characters import Warrior, Wizard


def main():
    nom1 = input("Entrez un nom: ")
    personnage1 = Wizard(nom1)
    print(personnage1)

    nom2 = input("Entrez un nom: ")
    personnage2 = Warrior(nom2)
    print(personnage2)
    print(personnage2.max_life)

    weapon, attack_points = personnage1.attack()
    print(weapon, attack_points)
    personnage2.defend(weapon, attack_points)
    print("Il reste " + str(personnage2.currentLife) + " points de vie à " + personnage2.nom)

    weapon, attack_points = personnage2.attack()
    print(weapon, attack_points)
    personnage1.defend(weapon, attack_points)
    print("Il reste " + str(personnage1.current_life) + " points de vie à " + personnage1.nom)


if __name__ == "__main__":
    main()
