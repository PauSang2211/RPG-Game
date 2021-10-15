# Level Up GUI
# Contains the GUI that tells the player that they have leveled up

from tkinter import *

class LevelUpGUI:
    def __init__(self, battleGUI, player):
        self.battleGUI = battleGUI
        self.player = player


        root = Tk()
        root.title("Level Up!")
        root.geometry("200x200")
        root.protocol("WM_DELETE_WINDOW", self.enable)
        self.myRoot = root
        self.myFrame = Frame(root)
        self.myFrame.grid()

        self.battleGUI.attackButton.config(state=DISABLED)
        self.battleGUI.openInventory.config(state=DISABLED)
        self.battleGUI.fleeButton.config(state=DISABLED)

        self.levelUpText = "Base HP: " + str(self.player.getMaxhp()) + " -> " + str(self.player.getMaxhp() + (2 + 2*(self.player.getLevel()-1))) + "\n"
        self.levelUpText += "Base Attack: " + str(self.player.getBaseAttack()) + " -> " + str(self.player.getBaseAttack() + (2 + 2*(self.player.getLevel()-1))) + "\n"
        self.levelUpText += "Base Defense: " + str(self.player.getBaseDefense()) + " -> " + str(self.player.getBaseDefense() + (2 + 2*(self.player.getLevel()-1))) + "\n"
        self.levelUpLabel = Label(self.myFrame, text=self.levelUpText)
        self.levelUpLabel.grid(row=0, column=0)

        self.player.levelUp()

    def enable(self):
        self.battleGUI.attackButton.config(state=ACTIVE)
        self.battleGUI.openInventory.config(state=ACTIVE)
        self.battleGUI.fleeButton.config(state=ACTIVE)

        self.myRoot.destroy()

