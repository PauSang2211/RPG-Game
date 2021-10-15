# File I/O Class
# grabs the information needed

from Backend.Items import Items
from Backend.Players import Players
from Backend.Enemies import Enemies
from Backend.Inventory import Inventory
from GUIs.BattleGUI import BattleGUI
from tkinter import *

class File:
    # reads a file and returns a list of the lines in the file
    def readFile(self, file):
        inputFile = open(file, "r")
        contents = []
        for line in inputFile:
            contents.append(line)
        inputFile.close()
        return contents

    # parse items and returns the Items class
    def grabItem(self):
        # prompt user for item file
        itemFile = input("Enter the item file: ")
        itemFile = "Files/" + itemFile
        contents = self.readFile(itemFile)

        # declare and initialize Items class
        items = Items()
        i = 1
        while not contents[i] == "<armor>\n":           # add all weapon(s)
            info = contents[i].split(",")
            items.addWeapon(info[0], info[1], info[2], info[3], info[4])
            i += 1

        i += 1      # increment once more to not look at "<armor>"
        while not contents[i] == "<consumable>\n":      # add all armor(s)
            info = contents[i].split(",")
            items.addArmor(info[0],info[1],info[2],info[3],info[4])
            i += 1

        i += 1      # increment once more to not look at "<consumable>"
        while not i == len(contents):                   # add all consumable(s)
            info = contents[i].split(",")
            items.addConsum(info[0],info[1],info[2],info[3],info[4])
            i += 1

        # return the items existing in the game
        return items

    # parse player data (stats and inventory) and return a list of Player class and Inventory class
    def playerStats(self, items):
        # prompt player file
        playerFile = input("Enter the player file: ")
        playerFile = "Files/" + playerFile
        contents = self.readFile(playerFile)

        # first line is the player's stats
        line = contents[0].split(",")
        player = Players(line[0],line[1],line[2],line[3],line[4],line[5],line[6])
        player.setImage("Files/" + contents[1])

        # initialize Inventory class
        inventory = Inventory()
        i = 2
        if i >= len(contents):
            return [player, inventory]
        elif i < len(contents) and contents[i] == "<weapon>\n":
            i = 3

        while i < len(contents) and not contents[i] == "<armor>\n" and not contents[i] == "<consumable>\n":           # add starting weapon(s)
            line = contents[i].split(",")
            if int(line[1]) > 0:
                inventory.add(items.find(line[0]), 0, line[1])
            i += 1

        if i >= len(contents):
            return [player, inventory]
        elif i < len(contents) and not contents[i] == "<consumable>\n":
            i += 1
        while i < len(contents) and not contents[i] == "<consumable>\n":      # add starting armor(s)
            line = contents[i].split(",")
            if int(line[1]) > 0:
                inventory.add(items.find(line[0]), 1, line[1])
            i += 1

        if i >= len(contents):
            return [player, inventory]
        elif i < len(contents):
            i += 1
        while not i >= len(contents):                   # add starting consumable(s)
            line = contents[i].split(",")
            if int(line[1]) > 0:
                inventory.add(items.find(line[0]), 2, line[1])
            i += 1

        return [player, inventory]

    # parse enemy data and return the Enemies class
    def enemystats(self, items):
        # prompt user for enemy file
        enemyFile = input("Enter the enemy file: ")
        enemyFile = "Files/" + enemyFile
        contents = self.readFile(enemyFile)

        # initialize Enemies class
        enemies = Enemies()
        for i in range(0, len(contents)):           # look at the necessary lines
            j = 0
            if contents[i] == "<enemy>\n":
                appearChance = contents[i+1]
                image = "Files/" + contents[i+2]
                stats = contents[i+3].split(",")

                j = i+4
                drops = {}
                if j >= len(contents):
                    enemies.addEnemy(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6], appearChance,
                                     image, drops)
                    break

                while not contents[j] == "<enemy>\n":
                    line = contents[j].split(",")
                    if items.find(line[1].strip()) and not line[1].strip() in drops.keys():
                        print("Adding " + line[1].strip() + "\tChance: " + line[0])
                        drops[line[1].strip()] = int(line[0])
                    j += 1

                enemies.addEnemy(stats[0], stats[1], stats[2], stats[3], stats[4], stats[5], stats[6], appearChance,
                                 image, drops)
            if not j == len(contents):
                i = j

        return enemies