import random
import webbrowser
from operator import itemgetter


# Classe Personnage

class Characters:

    max_life = 12
    max_sword_dice = 8
    max_magic_dice = 8
    max_bow_dice = 8
    bow_bonus = 0
    sword_bonus = 0
    magic_bonus = 0

    def __init__(self, name):
        self.name = name
        self._current_life = self.max_life
        self._height = random.randint(170, 190)
        self._weight = random.randint(70, 90)
        self._log = ""

    def attack(self):
        attack_results = self.roll_dice()
        attack_results = sorted(attack_results, key=itemgetter(1), reverse=True)
        if attack_results[0][0] == "Bow":
            attack_results[0][1] += self.bow_bonus
        if attack_results[0][0] == "Sword":
            attack_results[0][1] += self.sword_bonus
        return attack_results[0]

    def defend(self, weapon, attack_points):
        dices = dict(self.roll_dice())
        defence_points = dices[weapon]
        if defence_points < attack_points:
            damages = attack_points - defence_points
            self.current_life -= damages
        self.logs = " " + self.name + " defends for " + str(defence_points)
        return defence_points

    def heal(self):
        heal_chance = random.randint(0, 100)
        if 90 < heal_chance <= 100:
            self.current_life += self.max_life
            self.logs = " " + self.name + " heals for " + str(self.max_life)
            return 1
        elif 60 < heal_chance <= 90:
            self.current_life += self.max_life/2
            self.logs = " " + self.name + " heals for " + str(self.max_life/2)
            return 2
        elif 20 < heal_chance <= 60:
            self.current_life += self.max_life/4
            self.logs = " " + self.name + " heals for " + str(self.max_life/4)
            return 3
        elif 5 < heal_chance <= 20:
            self.logs = " " + self.name + " heals for 0"
            return 4
        else:
            self.current_life = 0
            self.logs = " " + self.name + " died from critical miss."
            return 5

    # Propriété Log

    def _get_log(self):
        temp = self._log
        self._log = ""
        return temp

    def _set_log(self, value):
        self._log += (" " + str(value) + " \n")

    logs = property(_get_log, _set_log)

    # Propriété Taille

    def _get_height(self):
        return self._height

    height = property(_get_height)

    # Propriété Poids

    def _get_weight(self):
        return self._weight

    weight = property(_get_weight)

    # Propriété Points de Vie

    def _get_current_life(self):
        return self._current_life

    def _set_current_life(self, value):
        self._current_life = max(min(self.max_life, value), 0)

    current_life = property(_get_current_life, _set_current_life)

    def roll_dice(self):
        sword_dice = random.randint(1, self.max_sword_dice)
        magic_dice = random.randint(1, self.max_magic_dice)
        bow_dice = random.randint(1, self.max_bow_dice)
        dices = [["Sword", sword_dice], ["Bow", bow_dice], ["Magic", magic_dice]]
        return dices

    def __repr__(self):
        return self.name + " the " + self.__class__.__name__


# Sous-classe Wizard


class Wizard(Characters):

    max_sword_dice = 8
    max_magic_dice = 12
    max_bow_dice = 10

    def attack(self):
        attack_results = super().attack()
        if attack_results[0] == "Magic":
            bonus_dice = random.randint(1, self.max_magic_dice)
            if bonus_dice > attack_results[1]:
                attack_results[1] = bonus_dice
        elif attack_results[0] == "Sword":
            attack_results[1] += (self._height + self._weight) // 40
        elif attack_results[0] == "Bow":
            attack_results[1] += (self._height - 170) % 3
        self.logs = " " + self.name + " attacks for " + str(attack_results)
        return attack_results


# Sous-classe Archer

class Archer(Characters):

    max_sword_dice = 10
    max_magic_dice = 8
    max_bow_dice = 12

    def attack(self):
        attack_results = super().attack()
        if attack_results[0] == ("Sword" or "Magic"):
            attack_results[1] += 1
            if attack_results[0] == "Sword":
                attack_results[1] += self._height // 40
            else:
                attack_results[1] += self._weight // 20
        self.logs = " " + self.name + " attacks for " + str(attack_results)
        return attack_results


# Sous-classe Warrior

class Warrior(Characters):

    max_sword_dice = 12
    max_magic_dice = 8
    max_bow_dice = 10
    max_life = 16

    def attack(self):
        attack_results = super().attack()
        if attack_results[0] == "Bow":
            attack_results[1] += (self._height - 170) % 3
        elif attack_results[0] == "Magic":
            attack_results[1] += self._weight // 30
        self.logs = " " + self.name + " attacks " + str(attack_results)
        return attack_results


# Classe race Elfe

class Elve:

    bow_bonus = 2
    sword_bonus = 0
    magic_bonus = 0


# Classe race Nain

class Dwarf:

    bow_bonus = 0
    sword_bonus = 2
    magic_bonus = 0


# Classe Nain Sorcier

class DwarfWizard(Wizard):
    def __init__(self, name):
        super().__init__(name)
        self.race = Dwarf()

    def as_html(self):
        return webbrowser.open("./html/DwarfWizard.html")


# Classe Nain Archer

class DwarfArcher(Archer):
    def __init__(self, name):
        super().__init__(name)
        self.race = Dwarf()

    def as_html(self):
        return webbrowser.open("./html/DwarfArcher.html")


# Classe Nain Guerrier

class DwarfWarrior(Warrior):
    def __init__(self, name):
        super().__init__(name)
        self.race = Dwarf()

    def as_html(self):
        return webbrowser.open("./html/DwarfWarrior.html")


# Classe Elfe Sorcier

class ElveWizard(Wizard):
    def __init__(self, name):
        super().__init__(name)
        self.race = Elve()

    def as_html(self):
        return webbrowser.open("./html/ElveWizard.html")


# Classe Elfe Archer

class ElveArcher(Archer):
    def __init__(self, name):
        super().__init__(name)
        self.race = Elve()

    def as_html(self):
        return webbrowser.open("./html/ElveArcher.html")


# Classe Elfe Guerrier

class ElveWarrior(Warrior):
    def __init__(self, name):
        super().__init__(name)
        self.race = Elve()

    def as_html(self):
        return webbrowser.open("./html/ElveWarrior.html")
