import random
from operator import itemgetter


# Classe Personnage

class Characters:

    max_life = 12
    max_sword_dice = 8
    max_magic_dice = 8
    max_bow_dice = 8

    def __init__(self, name):
        self.name = name
        self._current_life = self.max_life
        self._height = random.randint(170, 190)
        self._weight = random.randint(70, 90)

    def attack(self):
        dices = self.roll_dice()
        dices = sorted(dices, key=itemgetter(1), reverse=True)
        return dices[0]

    def defend(self, weapon, attack_points):
        dices = dict(self.roll_dice())
        defence_points = dices[weapon]
        if defence_points < attack_points:
            damages = attack_points - defence_points
            self.current_life -= damages
        return defence_points

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
        return self.name + " the " + self.__class__.__name__.lower()


# Race personnage

class Race:

    def __init__(self, race):
        self.race = race


# Sous-classe Wizard

class Wizard(Characters):

    max_sword_dice = 8
    max_magic_dice = 12
    max_bow_dice = 10

    def attack(self):
        dices = super().attack()
        if dices[0] == "Magic":
            bonus_dice = random.randint(1, self.max_magic_dice)
            if bonus_dice > dices[1]:
                dices[1] = bonus_dice
        elif dices[0] == "Sword":
            dices[1] += (self._height + self._weight) // 40
        elif dices[0] == "Bow":
            dices[1] += (self._height - 170) % 3
        return dices


# Sous-classe Archer

class Archer(Characters):

    max_sword_dice = 10
    max_magic_dice = 8
    max_bow_dice = 12

    def attack(self):
        dices = super().attack()
        if dices[0] == ("Sword" or "Magic"):
            dices[1] += 1
            if dices[0] == "Sword":
                dices[1] += self._height // 40
            else:
                dices[1] += self._weight // 20
        return dices


# Sous-classe Warrior

class Warrior(Characters):

    max_sword_dice = 12
    max_magic_dice = 8
    max_bow_dice = 10
    max_life = 16

    def attack(self):
        dices = super().attack()
        if dices[0] == "Bow":
            dices[1] += (self._height - 170) % 3
        elif dices[0] == "Magic":
            dices[1] += self._weight // 30
        return dices
