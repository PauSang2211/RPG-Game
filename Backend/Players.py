# Players Class
# A class that holds the player's data

class Players:
    def __init__(self, name, hp, level, exp, gold, attack, defense):
        self.__name = name
        self.__maxHp = int(hp)
        self.__hp = int(hp)
        self.__level = int(level)
        self.__exp = int(exp)
        self.__gold = int(gold)
        self.__attack = int(attack)
        self.__defense = int(defense)

        # level up the character if starting EXP exceeds level's Max HP
        self.levelUp()

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

    def getMaxExp(self):
        return 20 + 10*(self.__level - 1)

    def getGold(self):
        return self.__gold

    def getBaseAttack(self):
        return self.__attack

    # TODO: Gives the total attack after equipments
    def getAttack(self, inventory):
        weapon = inventory.getItem(inventory.getEquippedWeapon())
        armor = inventory.getItem(inventory.getEquippedArmor())

        if weapon == 0 and not armor == 0:
            return self.__attack + armor.getAttack()
        elif not weapon == 0 and armor == 0:
            return self.__attack + weapon.getAttack()
        elif weapon == 0 and armor == 0:
            print("attack normal")
            return self.__attack

        return self.__attack + weapon.getAttack() + armor.getAttack()

    def getBaseDefense(self):
        return self.__defense

    # TODO: Gives the total defense after equipments
    def getDefense(self, inventory):
        weapon = inventory.getItem(inventory.getEquippedWeapon())
        armor = inventory.getItem(inventory.getEquippedArmor())

        if weapon == 0 and not armor == 0:
            return self.__defense + armor.getDefense()
        elif not weapon == 0 and armor == 0:
            return self.__defense + weapon.getDefense()
        elif weapon == 0 and armor == 0:
            return self.__defense

        return self.__defense + weapon.getDefense() + armor.getDefense()

    def getImage(self):
        return self.__image

    def setMaxHp(self, newAmount):
        self.__maxHp = newAmount

    def setImage(self, file):
        self.__image = file.strip()

    def fullyHeal(self):
        self.__hp = self.__maxHp

    def increaseHp(self, amount):
        self.__hp += amount
        if self.__hp > self.__maxHp:
            self.__hp = self.__maxHp

    def decreaseHp(self, amount):
        self.__hp -= amount
        if self.__hp < 0:
            self.__hp = 0

    def increaseExp(self, amount):
        self.__exp += amount

    def canLevelUp(self):
        if self.__exp >= self.getMaxExp():
            return True
        return False

    def levelUp(self):
        while self.__exp >= self.getMaxExp():
            self.__exp = self.__exp - self.getMaxExp()
            self.__level += 1
            self.__maxHp += 2 + 2*(self.__level-2)
            self.__attack += 2 + 2*(self.__level-2)
            self.__defense += 2 + 2*(self.__level-2)


            print("Level Up!")
            print("Remaining EXP: " + str(self.__exp))

    def increaseGold(self, amount):
        self.__gold += amount
        print("Gold: " + str(self.__gold))

    def decreaseGold(self, amount):
        self.__gold -= amount
        print("Gold: " + str(self.__gold))

    def __str__(self):
        result = "Name: " + self.__name + "\n"
        result += "HP: " + str(self.__hp) + "\n"
        result += "Level: " + str(self.__level) + "\n"
        result += "EXP: " + str(self.__exp) + "\n"
        result += "Gold: " + str(self.__gold) + "\n"
        result += "Attack: " + str(self.__attack) + "\n"
        result += "Defense: " + str(self.__defense) + "\n"
        return result