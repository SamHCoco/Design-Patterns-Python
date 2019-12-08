from random import Random

from creational.factory.DarkMage import DarkMage
from creational.factory.Slime import Slime


class EnemyFactory:

    @staticmethod
    def create_enemy():
        number = Random().randint(0, 1)
        if number == 0:
            return DarkMage()
        if number == 1:
            return Slime()
