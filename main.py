# Pau Sang, psang@usc.edu
# ITP 499, Spring 2021
# Final Project
# Description:
# A GUI-based RPG game using classes 



from FileIO import File
from tkinter import *
from GUIs.BattleGUI import BattleGUI

def main():
    file = File()
    item = file.grabItem()
    player = file.playerStats(item)
    enemy = file.enemystats(item)


    root = Tk()
    battleGUI = BattleGUI(item, player[0], player[1], enemy, root)
    root.mainloop()

main()