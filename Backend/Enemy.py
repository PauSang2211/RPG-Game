# Enemy Class
# A class that holds the data for an enemy

class Enemy:
    def __init__(self, name, hp, level, exp, gold, attack, defense, appearChance, image, drops):
        self.__name = name
        self.__maxHp = int(hp)
        self.__hp = int(hp)
        self.__level = int(level)
        self.__exp = int(exp)
        self.__gold = int(gold)
        self.__attack = int(attack)
        self.__defense = int(defense)
        self.__appearChance = int(appearChance)
        self.__image = image.strip()
        self.__drops = drops


    def getName(self):
        return self.__name

    def getMaxhp(self):
        return self.__maxHp

    def getHp(self):
        return self.__hp

    def getLevel(self):
        return self.__level

    def getExp(self):
        return self.__exp

    def getGold(self):
        return self.__gold

    def getAttack(self):
        return self.__attack

    def getDefense(self):
        return self.__defense

    def getAppear(self):
        return self.__appearChance

    def getDrops(self):
        return self.__drops

    def getImage(self):
        return self.__image

    def decreaseHp(self, amount):
        self.__hp -= amount
        if self.__hp < 0:
            self.__hp = 0