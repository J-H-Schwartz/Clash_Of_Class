import random


class Wizard:

    def __init__(self, nom):
        self.classname = "Wizard"
        self.nom = nom
        self.maxLife = 12
        self.currentLife = 12
        self.swordDice = 0
        self.bowDice = 0
        self.magicDice = 0
        self.weapon = ""
        self.attack_points = 0
        self.defence_points = 0

    def attack(self):
        self.swordDice = random.randint(1, 8)
        self.bowDice = random.randint(1, 10)
        self.magicDice = random.randint(1, 12)
        if self.swordDice >= (self.bowDice & self.magicDice):
            self.weapon = "Sword"
            self.attack_points = self.swordDice
        elif self.bowDice >= (self.swordDice & self.magicDice):
            self.weapon = "Bow"
            self.attack_points = self.bowDice
        else:
            self.weapon = "Magic"
            self.attack_points = self.magicDice
            return self.weapon, self.attack_points

    def defend(self, weapon, attack_points):
        if weapon == "Sword":
            self.defence_points = random.randint(1, 8)
        elif weapon == "Bow":
            self.defence_points = random.randint(1, 10)
        else:
            self. defence_points = random.randint(1, 12)
        if self.defence_points < attack_points:
            self.currentLife -= (attack_points - self.defence_points)

    def __repr__(self):
        return self.nom + " the " + self.classname.lower()



nom = input("Entrez un nom: ")
objet = Wizard(nom)
print(objet)
