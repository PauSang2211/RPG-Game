# Item Class
# A class that defines an item


class Item:
    def __init__(self, name, attack, defense, hpboost, gold):
        self.__name = name
        self.__attack = int(attack)
        self.__defense = int(defense)
        self.__hpboost = int(hpboost)
        self.__gold = int(gold)

    def getName(self):
        return self.__name

    def getAttack(self):
        return self.__attack

    def getDefense(self):
        return self.__defense

    def getHpboost(self):
        return self.__hpboost

    def getGold(self):
        return self.__gold

    def __str__(self):
        result = "Name: " + self.__name + "\n"
        result += "Attack: " + str(self.__attack) + "\n"
        result += "Defense: " + str(self.__defense) + "\n"
        result += "HP Boost: " + str(self.__hpboost) + "\n"
        result += "Sell Price: " + str(self.__gold) + "\n"
        return result