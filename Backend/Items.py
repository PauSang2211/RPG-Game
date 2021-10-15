# Item Class
# A class that stores all the items available in the game

from Backend.Item import Item

class Items:
    def __init__(self):
        self.__weapons = {}
        self.__armors = {}
        self.__consums = {}
        self.__allItems = {}


    def getWeapons(self):
        return self.__weapons

    def getArmors(self):
        return self.__armors

    def getConsums(self):
        return self.__consums


    def addWeapon(self, name, attack, defense, hpboost, gold):
        weapon = Item(name, attack, defense, hpboost, gold)
        self.__weapons[name] = weapon
        self.__allItems[name] = weapon

    def addArmor(self, name, attack, defense, hpboost, gold):
        armor = Item(name, attack, defense, hpboost, gold)
        self.__armors[name] = armor
        self.__allItems[name] = armor

    def addConsum(self, name, attack, defense, hpboost, gold):
        consum = Item(name, attack, defense, hpboost, gold)
        self.__consums[name] = consum
        self.__allItems[name] = consum

    def find(self, name):
        return self.__allItems[name]

    def findType(self, name):
        if name in self.__weapons:
            return 0
        elif name in self.__armors:
            return 1
        elif name in self.__consums:
            return 2
        return 3