# Inventory Class
# A class that holds the player's items

class Inventory:
    def __init__(self):
        self.__items = {}
        self.__weapons = set()
        self.__armors = set()
        self.__consums = set()
        self.__equippedWeapon = ""
        self.__equippedArmor = ""

    def get(self):
        return self.__items

    def getEquippedWeapon(self):
        return self.__equippedWeapon

    def getEquippedArmor(self):
        return self.__equippedArmor

    def getItem(self, itemName):
        if itemName in self.__items:
            return self.__items[itemName][0]
        return 0

    def getItemCount(self, itemName):
        return self.__items[itemName][1]

    def deleteItem(self, itemName):
        self.__items.pop(itemName)
        print("Item removing: " + itemName)
        if self.findType(itemName) == 0:
            self.__weapons.remove(itemName)
        elif self.findType(itemName) == 1:
            self.__armors.remove(itemName)
        else:
            self.__consums.remove(itemName)

    def setWeapon(self, itemName):
        self.__equippedWeapon = itemName

    def setArmor(self, itemName):
        self.__equippedArmor = itemName

    def findType(self, itemName):
        if itemName in self.__weapons:
            return 0
        elif itemName in self.__armors:
            return 1
        elif itemName in self.__consums:
            return 2
        return 3

    def add(self, item, type, count):
        if item.getName() in self.__items:
            self.__items[item.getName()][1] += 1
            return

        self.__items[item.getName()] = [item, int(count)]
        if type == 0:
            self.__weapons.add(item.getName())
            if self.__equippedWeapon == "":
                self.__equippedWeapon = item.getName()
        elif type == 1:
            self.__armors.add(item.getName())
            if self.__equippedArmor == "":
                self.__equippedArmor = item.getName()
        elif type == 2:
            self.__consums.add(item.getName())

    def increaseCount(self, itemName):
        self.__items[itemName][1] += 1

    def decreaseCount(self, itemName):
        self.__items[itemName][1] -= 1

    def __str__(self):
        items = list(self.__items.values())
        result = ""
        for item in items:
            result += "Name: " + item[0].getName() + "\n"
            result += "\tAttack: " + str(item[0].getAttack()) + "\n"
            result += "\tDefense: " + str(item[0].getDefense()) + "\n"
            result += "\tHP Boost: " + str(item[0].getHpboost()) + "\n"
            result += "\tGold: " + str(item[0].getGold()) + "\n"

        return result