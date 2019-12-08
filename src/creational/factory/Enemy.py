class Enemy:

    def __init__(self, species):
        self.species = species
        self.attack()

    def attack(self):
        print("{} attacks you!".format(self.species))
