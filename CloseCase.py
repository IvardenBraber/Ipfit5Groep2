from tkinter import *
from tkinter import ttk

gui = Tk()
gui.geometry("500x450")

# newCase_label = Label(gui, text="Close HOAX", width=14, font=("bold", 15))
# newCase_label.place(x=170, y=53)

a = Label(gui, text="Are you sure you want to close the tool?", width=40)
a.place(x=80,y=130)

e = ttk.Button(gui, text="YES", width=10)
e.place(x=195, y=350)

f = ttk.Button(gui, text="NO", width=10)
f.place(x=120,y=350)



gui.mainloop()