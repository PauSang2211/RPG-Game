# BattleGUI Class
# Creates the GUI for the battlefield

from tkinter import *
from tkinter import messagebox
from GUIs.InventoryGUI import InventoryGUI
from GUIs.RewardGUI import RewardGUI
import random


class BattleGUI:
    def __init__(self, items, player, inventory, enemies, root=None):
        self.items = items
        self.player = player
        self.inventory = inventory
        self.enemies = enemies

        self.myRoot = root
        self.myRoot.title("Game")
        self.myRoot.geometry("550x300")
        self.myFrame = Frame(root)
        self.myFrame.grid()

        # InventoryGUI
        self.inventoryGUI = InventoryGUI(self, self.player, self.inventory)

        # Create a list of images
        self.images = {}
        self.images[self.player.getImage()] = PhotoImage(file=self.player.getImage())
        for enemy in self.enemies.getEnemies().values():
            self.images[enemy.getImage()] = PhotoImage(file=enemy.getImage())

        self.playerNameLabel = Label(self.myFrame, text=self.player.getName())
        self.playerNameLabel.grid(row=0, column=0)

        self.playerHP = StringVar()
        self.playerHP.set("HP: " + str(self.player.getHp()) + "/" + str(self.player.getMaxhp()))
        self.playerHPLabel = Label(self.myFrame, textvariable=self.playerHP)
        self.playerHPLabel.grid(row=1, column=0)

        self.playerLevel = StringVar()
        self.playerLevel.set("Level: " + str(self.player.getLevel()))
        self.playerLevelLabel = Label(self.myFrame, textvariable=self.playerLevel)
        self.playerLevelLabel.grid(row=2, column=0)

        self.playerImageLabel = Label(self.myFrame, image=self.images[self.player.getImage()])
        self.playerImageLabel.grid(row=3, column=0, rowspan=3, columnspan=2)

        self.currentEnemy = self.enemies.getRandEnemy()
        self.enemyName = StringVar()
        self.enemyName.set(self.currentEnemy.getName())
        self.enemyNameLabel = Label(self.myFrame, textvariable=self.enemyName)
        self.enemyNameLabel.grid(row=0, column=5)

        self.enemyHP = StringVar()
        self.enemyHP.set("HP: " + str(self.currentEnemy.getHp()) + "/" + str(self.currentEnemy.getMaxhp()))
        self.enemyHPLabel = Label(self.myFrame, textvariable=self.enemyHP)
        self.enemyHPLabel.grid(row=1, column=5)

        self.enemyLevel = StringVar()
        self.enemyLevel.set("Level: " + str(self.currentEnemy.getLevel()))
        self.enemyLevelLabel = Label(self.myFrame, textvariable=self.enemyLevel)
        self.enemyLevelLabel.grid(row=2, column=5)

        self.enemyImageLabel = Label(self.myFrame, image=self.images[self.currentEnemy.getImage()])
        self.enemyImageLabel.grid(row=3, column=4, rowspan=3, columnspan=2)

        self.attackButton = Button(self.myFrame, text="ATTACK", command=self.attackEnemy)
        self.attackButton.grid(row=6, column=0, columnspan=2)

        self.openInventory = Button(self.myFrame, text="OPEN INVENTORY", command=self.make_inventory)
        self.openInventory.grid(row=6, column=2, columnspan=2)

        self.fleeButton = Button(self.myFrame, text="FLEE", command=self.changeEnemy)
        self.fleeButton.grid(row=6, column=4, columnspan=2)

    def main_page(self):
        self.myFrame.grid()

    def make_inventory(self):
        self.myFrame.grid_forget()
        self.inventoryGUI.setInventory(self.inventory)
        self.inventoryGUI.myFrame.tkraise()
        self.inventoryGUI.myFrame.pack()


    def attackEnemy(self):
        # For readability, put in diff variables
        playerAttack = self.player.getAttack(self.inventory)
        enemyDefense = self.currentEnemy.getDefense()
        totalAttack = playerAttack - enemyDefense
        print("Player Attacks Enemy: " + str(playerAttack) + " - " + str(enemyDefense))
        if totalAttack < 0:
            totalAttack = 0

        # Update enemy stats and GUI
        self.currentEnemy.decreaseHp(totalAttack)
        self.enemyHP.set("HP: " + str(self.currentEnemy.getHp()) + "/" + str(self.currentEnemy.getMaxhp()))

        if self.currentEnemy.getHp() == 0:
            rewardGUI = RewardGUI(self, self.items, self.player, self.currentEnemy, self.inventory)

        else:
            # Enemy attacks
            enemyAttack = self.currentEnemy.getAttack()
            playerDefense = self.player.getDefense(self.inventory)
            totalAttack = enemyAttack - playerDefense
            print("Enemy Attacks Player: " + str(enemyAttack) + " - " + str(playerDefense) + "\n")
            if totalAttack < 0:
                totalAttack = 0

            # Update player stats and GUI
            self.player.decreaseHp(totalAttack)
            self.playerHP.set("HP: " + str(self.player.getHp()) + "/" + str(self.player.getMaxhp()))

            if self.player.getHp() == 0:
                self.attackButton.config(state=DISABLED)
                self.openInventory.config(state=DISABLED)
                self.fleeButton.config(state=DISABLED)
                messagebox.showerror('R.I.P', "You are dead!")



    def changeEnemy(self):
        self.currentEnemy = self.enemies.getRandEnemy()         # Object
        self.enemyName.set(self.currentEnemy.getName())
        self.enemyHP.set("HP: " + str(self.currentEnemy.getHp()) + "/" + str(self.currentEnemy.getMaxhp()))
        self.enemyLevel.set("Level: " + str(self.currentEnemy.getLevel()))
        self.enemyImageLabel.config(image=self.images[self.currentEnemy.getImage()])


    def changeFrame(self, frame):
        if frame == self.inventoryGUI:
            self.inventoryGUI.setInventory(self.inventory)
        frame.myFrame.tkraise()









