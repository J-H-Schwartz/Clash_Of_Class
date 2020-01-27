import random
from operator import itemgetter


# Classe Personnage

class Characters:

    max_life = 12
    max_sword_dice = 8
    max_magic_dice = 8
    max_bow_dice = 8

    def __init__(self, nom):
        self.nom = nom
        self.current_life = self.max_life

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

    def roll_dice(self):
        sword_dice = random.randint(1, self.max_sword_dice)
        magic_dice = random.randint(1, self.max_magic_dice)
        bow_dice = random.randint(1, self.max_bow_dice)
        dices = [["Sword", sword_dice], ["Bow", bow_dice], ["Magic", magic_dice]]
        return dices

    def __repr__(self):
        return self.nom + " the " + self.__class__.__name__.lower()


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
        return dices


# Sous-classe Warrior

class Warrior(Characters):

    max_sword_dice = 12
    max_magic_dice = 8
    max_bow_dice = 10
    max_life = 16
