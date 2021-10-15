# Enemies Class
# A class that holds that data for all enemies

import random
from Backend.Enemy import Enemy

class Enemies:
    def __init__(self):
        self.__enemies = {}
        self.__appearChances = {}

    def getEnemies(self):
        return self.__enemies

    def getRandEnemy(self):
        randEnemy = random.choices(list(self.__appearChances.keys()), weights=tuple(self.__appearChances.values()))
        randEnemy = self.__enemies[randEnemy[0]]
        randEnemy = Enemy(randEnemy.getName(), randEnemy.getHp(), randEnemy.getLevel(),
                          randEnemy.getExp(), randEnemy.getGold(), randEnemy.getAttack(),
                          randEnemy.getDefense(), randEnemy.getAppear(), randEnemy.getImage(),
                          randEnemy.getDrops())
        return randEnemy

    def addEnemy(self, name, hp, level, exp, gold, attack, defense, appearChance, image, drops):
        enemy = Enemy(name, hp, level, exp, gold, attack, defense, appearChance, image, drops)
        self.__enemies[name] = enemy
        self.__appearChances[name] = int(appearChance)