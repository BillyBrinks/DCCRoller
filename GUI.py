from tkinter import *
from Character import *

root = Tk()
root.title('Dungeon Crawl Classics')
root.geometry('1000x600')
button = Button(root, text="Generate 4 Character Sheets", bg='black', fg='green', padx=5, pady=5,
                font="Courier").grid(row=0, column=0)

c = Character()
sheet = Text(root)
s = c.getInfo()
sheet.insert(INSERT, s)
sheet.grid(row=1, column=0)


root.mainloop()