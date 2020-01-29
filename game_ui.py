import webbrowser
from characters import ElveWarrior, ElveWizard, ElveArcher, DwarfWarrior, DwarfWizard, DwarfArcher


class GameUi:

    def __init__(self):
        while True:
            game_menu = input("(C)ommencer la partie / (L)exique des personnages").upper()
            if game_menu == "C":
                self.characters_selection()
                return
            elif game_menu == "L":
                while True:
                    characters_info_menu = input("Quel personnage souhaitez-vous consulter ?\n Dwarf Wizard (1) /"
                                                 " Dwarf Archer (2) / Dwarf Warrior (3)\n Elve Wizard (4) / Elve Archer (5)"
                                                 " / Elve Warrior (6)\n (Q)uitter").upper()
                    if characters_info_menu == "1":
                        webbrowser.open("./html/DwarfWizard.html")
                        continue
                    elif characters_info_menu == "2":
                        webbrowser.open("./html/DwarfArcher.html")
                        continue
                    elif characters_info_menu == "3":
                        webbrowser.open("./html/DwarfWarrior.html")
                        continue
                    elif characters_info_menu == "4":
                        webbrowser.open("./html/ElveWizard.html")
                        continue
                    elif characters_info_menu == "5":
                        webbrowser.open("./html/ElveArcher.html")
                        continue
                    elif characters_info_menu == "6":
                        webbrowser.open("./html/ElveWarrior.html")
                        continue
                    elif characters_info_menu == "Q":
                        print("Retour au menu précédent.")
                        break
                    else:
                        print("Commande invalide, recommencez.")
                continue
            else:
                print("Commande Invalide, recommencez.")


    def characters_selection(self):
        character = []
        i = 0
        while i < 2:
            name = input("Entrez un nom: ")
            while True:
                while True:
                    race = input("Choisissez la race de votre personnage: (D)warf / (E)lve: ").upper()
                    if race == "D":
                        break
                    elif race == "E":
                        break
                    else:
                        print("Veuillez choisir une race valide.")
                        continue
                while True:
                    character_class = input(
                        "Quelle classe voulez-vous jouer ? (W)izard / (A)rcher / Wa(R)rior: ").upper()
                    if character_class == "W":
                        break
                    elif character_class == "A":
                        break
                    elif character_class == "R":
                        break
                    else:
                        print("Veuillez choisir une classe valide.")

                if race == "E" and character_class == "W":
                    choice = ElveWizard
                    break
                elif race == "E" and character_class == "A":
                    choice = ElveArcher
                    break
                elif race == "E" and character_class == "R":
                    choice = ElveWarrior
                    break
                elif race == "D" and character_class == "W":
                    choice = DwarfWizard
                    break
                elif race == "D" and character_class == "A":
                    choice = DwarfArcher
                    break
                elif race == "D" and character_class == "R":
                    choice = DwarfWarrior
                    break
                else:
                    print("La configuration du personnage a échoué. Veuillez recommencer.")

            print(choice(name))
            character.append(choice(name))
            i += 1
        player1 = character[0]
        player2 = character[1]
        self.start_game_menu(player1, player2)
        return

    def start_game_menu(self, player1, player2):
        while True:
            character_inspection = input("Souhaitez vous voir la fiche de votre personnage ou débuter la partie ? {} "
                                         "(1) / {} (2) / (C)ommencer".format(player1.name, player2.name)).upper()
            if character_inspection == "1":
                player1.as_html()
                continue
            elif character_inspection == "2":
                player2.as_html()
                continue
            elif character_inspection == "C":
                self.start_fight(player1, player2)
                return
            else:
                print("Commande invalide, recommencez.")

    def start_fight(self, player1, player2):
        attacker = player1
        defender = player2
        print("")
        while player1.current_life > 0 and player2.current_life > 0:

            print("Au début de ce tour il reste {} points de vie à {}.".format(int(defender.current_life),
                                                                               defender.name))
            weapon, attack_points = attacker.attack()
            print(attacker.name + " frappe pour " + str(attack_points) + " points de dégats.")
            defence_points = defender.defend(weapon, attack_points)
            print(defender.name + " se défend pour pour " + str(defence_points) + " points de dégats.")
            damages_difference = attack_points - defence_points
            if damages_difference > 0:
                print("{} inflige {} points de dégats à {}.".format(attacker.name, damages_difference,
                                                                    defender.name))
            else:
                print("{} pare le coup porté par {}".format(defender, attacker))
            print("Il reste " + str(int(defender.current_life)) + " points de vie à " + defender.name)
            if defender.current_life == 0:
                break
            heal_try = defender.heal()
            if heal_try == 1:
                print(
                    "{} essaye de se soigner. Soins Critique ! Sa vie remonte au maximum. Il est désormais à {} points de"
                    " vie.\n".format(defender.name, int(defender.current_life)))
            elif heal_try == 2:
                print("{} essaye de se soigner. Réussite. Il regagne la moitié de son maximum de PV. "
                      "Il est désormais à {} points de vie.\n".format(defender.name, int(defender.current_life)))
            elif heal_try == 3:
                print(
                    "{} essaye de se soigner. Le sort réussit, mais avec beaucoup de difficultés. Il regagne un quart de"
                    " son maximum de PV. Il est désormais à {} points de vie.\n".format(defender.name,
                                                                                        int(defender.current_life)))
            elif heal_try == 4:
                print("{} essaye de se soigner. Le sort échoue.\n".format(defender.name))
            else:
                print("{} essaye de se soigner. Echec Critique ! Décès inopiné. (Pauvre naze)\n".format(defender.name))

            if attacker == player1:
                attacker = player2
                defender = player1
            else:
                attacker = player1
                defender = player2

        if player1.current_life == 0:
            print(player2.name + " gagne la partie.")
            return
        if player2.current_life == 0:
            print(player1.name + " gagne la partie.")
            return