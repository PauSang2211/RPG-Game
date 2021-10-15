# RewardGUI Class
# Provides the visual for the reward system and updates the player's inventory and stats accordingly

from tkinter import *
from GUIs.LevelUpGUI import LevelUpGUI
import random

class RewardGUI:
    def __init__(self, battleGUI, items, player, currentEnemy, inventory):
        self.battleGUI = battleGUI
        self.items = items
        self.player = player
        self.inventory = inventory
        self.currentEnemy = currentEnemy

        # Disable attack, inventory, and flee buttons
        self.battleGUI.attackButton.config(state=DISABLED)
        self.battleGUI.openInventory.config(state=DISABLED)
        self.battleGUI.fleeButton.config(state=DISABLED)

        root = Tk()
        root.title("Congratulations!")
        root.geometry("200x100")
        root.protocol("WM_DELETE_WINDOW", self.update)
        self.myRoot = root
        self.myFrame = Frame(root)
        self.myFrame.grid()

        self.rewardText = "+" + str(self.currentEnemy.getExp()) + " EXP\n"
        self.rewardText += "+" + str(self.currentEnemy.getGold()) + " Gold\n"
        self.randLoot()
        for reward in self.rewards:
            self.rewardText += "+1 " + reward + "\n"

        self.rewardLabel = Label(self.myFrame, text=self.rewardText)
        self.rewardLabel.grid(row=0, column=0)

    def update(self):
        self.player.increaseExp(self.currentEnemy.getExp())
        self.player.increaseGold(self.currentEnemy.getGold())

        for reward in self.rewards:
            if self.items.findType(reward) != 3:
                self.inventory.add(self.items.find(reward), self.items.findType(reward), 1)
            else:
                print("ERROR! ITEM DOES NOT EXIST!")

        self.myRoot.destroy()

        canLevelUp = self.player.canLevelUp()
        if canLevelUp:
            levelUpGUI = LevelUpGUI(self.battleGUI, self.player)
        else:
            self.battleGUI.attackButton.config(state=ACTIVE)
            self.battleGUI.openInventory.config(state=ACTIVE)
            self.battleGUI.fleeButton.config(state=ACTIVE)
        self.battleGUI.changeEnemy()
        self.player.fullyHeal()
        self.battleGUI.playerHP.set("HP: " + str(self.player.getHp()) + "/" + str(self.player.getMaxhp()))

        if canLevelUp:
            self.battleGUI.playerLevel.set("Level: " + str(self.player.getLevel()))

    def randLoot(self):
        allDrops = self.currentEnemy.getDrops()
        dropKeys = list(self.currentEnemy.getDrops().keys())
        self.rewards = []
        for drop in dropKeys:
            chance = random.randrange(0, 100)
            if chance <= allDrops[drop]:
                self.rewards.append(drop.strip())
                print("You got " + drop.strip())
            else:
                print("You did not get " + drop.strip())
