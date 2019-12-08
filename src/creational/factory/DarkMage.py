from creational.factory.Enemy import Enemy


class DarkMage(Enemy):

    def __init__(self):
        super().__init__("Dark Mage")

    def attack(self):
        print("{} attacks you with DARK LIGHTNING!\nYou lose 10 HP.\n".format(self.species))
