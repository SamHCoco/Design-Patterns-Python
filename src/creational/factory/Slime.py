from creational.factory.Enemy import Enemy


class Slime(Enemy):

    def __init__(self):
        super().__init__("Slime")

    def attack(self):
        print("{} uses WEIRD LICK!\nYou lose 1 HP but gain a friend.\n".format(self.species))
