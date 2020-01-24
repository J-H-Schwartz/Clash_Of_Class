import random
from operator import itemgetter


# Classe Personnage

class Characters:

    def __init__(self):
        self.nom = ""
        self.max_life = 12
        self.current_life = 12
        self.sword_dice = 0
        self.bow_dice = 0
        self.magic_dice = 0
        self.weapon = ""
        self.attack_points = 0
        self.defence_points = 0
        self.dices = []
        self.max_sword_dice = 0
        self.max_magic_dice = 0
        self.max_bow_dice = 0

    def attack(self):
        sword_dice = random.randint(1, self.max_sword_dice)
        bow_dice = random.randint(1, self.max_bow_dice)
        magic_dice = random.randint(1, self.max_magic_dice)
        dices = [["Sword", sword_dice], ["Bow", bow_dice], ["Magic", magic_dice]]
        dices = sorted(dices, key=itemgetter(1), reverse=True)
        return dices[0]

    def defend(self, weapon, attack_points):
        if weapon == "Sword":
            defence_points = random.randint(1, self.max_sword_dice)
        elif weapon == "Bow":
            defence_points = random.randint(1, self.max_bow_dice)
        else:
            defence_points = random.randint(1, self.max_magic_dice)
        if defence_points < attack_points:
            damages = attack_points - defence_points
            self.current_life -= damages

    def __repr__(self):
        return self.nom + " the " + self.__class__.__name__.lower()


# Sous-classe Wizard

class Wizard(Characters):

    def __init__(self, nom):
        super().__init__()
        self.nom = nom
        self.max_sword_dice = 8
        self.max_magic_dice = 12
        self.max_bow_dice = 10

    def attack(self):
        dices = super().attack()
        if dices[0] == "Magic":
            bonus_dice = random.randint(1, self.max_magic_dice)
            if bonus_dice > dices[1]:
                dices[1] = bonus_dice
        return dices

    def __repr__(self):
        return self.nom + " the " + self.__class__.__name__.lower()


# Sous-classe Archer

class Archer(Characters):

    def __init__(self, nom):
        super().__init__()
        self.nom = nom
        self.max_sword_dice = 10
        self.max_magic_dice = 8
        self.max_bow_dice = 12

    def attack(self):
        dices = super().attack()
        if dices[0] == ("Sword" or "Magic"):
            dices[1] += 1
        return dices

    def __repr__(self):
        return self.nom + " the " + self.__class__.__name__.lower()


# Sous-classe Warrior

class Warrior(Characters):

    def __init__(self, nom):
        super().__init__()
        self.nom = nom
        self.max_sword_dice = 12
        self.max_magic_dice = 8
        self.max_bow_dice = 10
        self.max_life = 16
        self.currentLife = 16

    def __repr__(self):
        return self.nom + " the " + self.__class__.__name__.lower()
