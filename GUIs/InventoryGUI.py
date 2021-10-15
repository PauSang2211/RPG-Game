# InventoryGUI Class
# Provides the GUI for the inventory

from tkinter import *

class InventoryGUI():

    def __init__(self, battleGUI, player, inventory):
        self.battleGUI = battleGUI
        self.player = player
        self.inventory = inventory

        self.myFrame = Frame(self.battleGUI.myRoot)

        self.currItem = ""
        self.defaultInfoText = "Name: N/A\nAttack: N/A\nDefense: N/A\nHP Boost: N/A\nSell Price: N/A\nCount: N/A"
        self.infoText = StringVar()
        self.infoText.set(self.defaultInfoText)
        self.equipText = StringVar()
        self.equipText.set("N/A")

        self.info = Label(self.myFrame, textvariable=self.infoText)
        self.info.pack(fill='x', ipady=10, expand=True)

        self.sellButton = Button(self.myFrame, text="Sell", command=self.sellItem)
        self.sellButton.config(state=DISABLED)
        self.sellButton.pack(fill='x', ipadx=10)

        self.equipButton = Button(self.myFrame, textvariable=self.equipText, command=self.equipItem)
        self.equipButton.config(state=DISABLED)
        self.equipButton.pack(fill='x', ipadx=10)

        self.goBackButton = Button(self.myFrame, text="Go Back", command=self.goBack)
        self.goBackButton.pack()

        items = self.inventory.get().keys()
        print("Initial items:")
        print(items)
        self.scrollbar = Scrollbar(self.myFrame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.itemListbox = Listbox(self.myFrame, width=26)
        for item in items:
            self.itemListbox.insert(END, item)
        self.itemListbox.pack()
        self.scrollbar.config(command=self.itemListbox.yview())
        self.itemListbox.bind('<<ListboxSelect>>', self.displayInfo)

    def goBack(self):
        self.myFrame.pack_forget()
        self.battleGUI.myFrame.tkraise()
        self.battleGUI.myFrame.grid()

    def setInventory(self, inventory):
        self.inventory = inventory
        self.itemListbox.delete(0, END)
        items = self.inventory.get().keys()
        for item in items:
            self.itemListbox.insert(END, item)


    def displayInfo(self, Event=None):
        ndex = self.itemListbox.curselection()
        if ndex != ():
            item = self.inventory.get()
            item = item[self.itemListbox.get(self.itemListbox.curselection())][0]
            count = self.inventory.getItemCount(item.getName())
            self.infoText.set(str(item) + "Count: " + str(count))
            self.currItem = item.getName()
            if self.inventory.findType(item.getName()) == 0:
                if self.inventory.getEquippedWeapon() == "" or self.inventory.getEquippedWeapon() != item.getName():
                    self.equipText.set("Equip")
                    self.equipButton.config(state=ACTIVE)
                    self.sellButton.config(state=ACTIVE)
                else:
                    self.equipText.set("Equipped")
                    self.equipButton.config(state=DISABLED)

                    if count == 1:
                        self.sellButton.config(state=DISABLED)
                    else:
                        self.sellButton.config(state=ACTIVE)
            elif self.inventory.findType(item.getName()) == 1:
                if self.inventory.getEquippedArmor() == "" or self.inventory.getEquippedArmor() != item.getName():
                    self.equipText.set("Equip")
                    self.equipButton.config(state=ACTIVE)
                    self.sellButton.config(state=ACTIVE)
                else:
                    self.equipText.set("Equipped")
                    self.equipButton.config(state=DISABLED)

                    if count == 1:
                        self.sellButton.config(state=DISABLED)
                    else:
                        self.sellButton.config(state=ACTIVE)
            else:
                self.equipText.set("Use")
                self.equipButton.config(state=ACTIVE)
                self.sellButton.config(state=ACTIVE)

    def sellItem(self):
        self.inventory.decreaseCount(self.currItem)
        self.player.increaseGold(self.inventory.getItem(self.currItem).getGold())
        self.displayInfo()
        if self.inventory.getItemCount(self.currItem) == 0:
            self.itemListbox.delete(self.itemListbox.curselection())
            self.inventory.deleteItem(self.currItem)
            self.infoText.set(self.defaultInfoText)
            self.sellButton.config(state=DISABLED)
            self.equipButton.config(state=DISABLED)

    def equipItem(self):
        count = self.inventory.getItemCount(self.currItem)

        if self.inventory.findType(self.currItem) == 0:
            self.inventory.setWeapon(self.currItem)
            self.equipText.set("Equipped")
            self.equipButton.config(state=DISABLED)

            if count == 1:
                self.sellButton.config(state=DISABLED)
        elif self.inventory.findType(self.currItem) == 1:
            self.inventory.setArmor(self.currItem)
            self.equipText.set("Equipped")
            self.equipButton.config(state=DISABLED)

            if count == 1:
                self.sellButton.config(state=DISABLED)
        else:
            self.player.increaseHp(self.inventory.getItem(self.currItem).getHpboost())
            self.inventory.decreaseCount(self.currItem)
            count -= 1
            if count == 0:
                self.itemListbox.delete(self.itemListbox.curselection())
                self.inventory.deleteItem(self.currItem)
                self.infoText.set(self.defaultInfoText)
                self.sellButton.config(state=DISABLED)
                self.equipButton.config(state=DISABLED)
        self.battleGUI.playerHP.set("HP: " + str(self.player.getHp()) + "/" + str(self.player.getMaxhp()))