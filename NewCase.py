from tkinter import *
from tkinter import ttk
from case import case

gui = Tk()
gui.geometry("600x550")

newCase_label = Label(gui, text="New Case", width=14, font=("bold", 15))
newCase_label.place(x=170, y=53)

a = Label(gui, text="Case Name:", width=10)
a.place(x=70,y=130)

ab = Entry(gui)
ab.place(x=185, y=130)

c = Label(gui, text="Case Folder:", width=12)
c.place(x=60, y=180)

cb = Entry(gui)
cb.place(x=185, y=180)

d = Label(gui, text="Case Summary:", width=13)
d.place(x=65, y=230)

db = Entry(gui)
db.place(x=185, y=230)

##serienummer, nummer van image, nummer mediadrager toevoegen
b = Label(gui, text="Serialnumber: ", width=13)
b.place(x=62, y=280)

bb = Entry(gui)
bb.place(x=185, y=280)

g = Label(gui, text="Image number: ", width=14)
g.place(x=62, y=330)

gb = Entry(gui)
gb.place(x=185, y=330)

h = Label(gui, text="Data carrier number: ", width=21)
h.place(x=50, y=380)

hb = Entry(gui)
hb.place(x=185, y=380)

cInfo = ab.get()
cFolder = cb.get()
cSummary = db.get()
cSNumber = bb.get()
cINumber = gb.get()
cDCNumber = hb.get()

e = ttk.Button(gui, text="Create Case", width=11, command=(case(cInfo, cFolder, cSummary, cSNumber, cINumber, cDCNumber)))
e.place(x=195, y=430)

f = ttk.Button(gui, text="Go Back", width=7)
f.place(x=120, y=430)


gui.mainloop()