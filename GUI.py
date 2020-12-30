from tkinter import *
from Character import *

root = Tk()
root.title('Dungeon Crawl Classics Character Generator')
root.geometry('1000x600')

def displayInfo():
    c = Character()
    HP = Label(root, text=f'HP: {c.HP}')
    HP.pack()
    XP = Label(root, text=f'XP: {c.XP}')
    XP.pack()
    AC = Label(root, text=f'Armor Class: {c.AC}')
    AC.pack()
    Coppahs = Label(root, text=f'Coppahs: {c.coppahs}')
    Coppahs.pack()
    BALR = Label(root, text=f'Birth Augr & Lucky Roll: {c.BALR}')
    BALR.pack()
    Occ = Label(root, text=f'Occupation: {c.occupation}')
    Occ.pack()
    Inv = Label(root, text=f'Inventory: {c.inventory}')
    Inv.pack()
    for ability in c.abilities:
        abil = Label(root, text=f'\n{ability}: {c.abilities.get(ability)}')
        abil.pack()
        mod = Label(root, text=f'Modifier: {c.modifiers.get(ability)}\n')
        mod.pack()


button = Button(root, text="Generate Character", command=displayInfo)
button.pack()

root.mainloop()

