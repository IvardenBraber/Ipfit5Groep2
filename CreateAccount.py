from tkinter import *
from tkinter import ttk
#import tkinter as tk -> nodig voor tk.CENTER, nu niet in gebruik
gui = Tk()
gui.geometry("460x350")

s = ttk.Style()
s.theme_names()
s.theme_use('clam')

gui.title("HOAX")

a = Label(gui, text="Username: ")
a.grid(row=2, column=0)

b = Label(gui, text="Password: ")
b.grid(row=4, column=0)

c = ttk.Button(gui, text="Register account")
c.grid(row=6, column=0)

E = Entry(gui).grid(row=2,column=3)
F = Entry(gui).grid(row=4, column=3)


positionRight = int(gui.winfo_screenwidth() / 2 - gui.winfo_reqwidth() / 2)
positionDown = int(gui.winfo_screenheight() / 3 - gui.winfo_reqheight() / 2)

# Positions the window in the center of the page.
gui.geometry("+{}+{}".format(positionRight, positionDown))


gui.mainloop()