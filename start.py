from tkinter import *
from tkinter import ttk
#import tkinter as tk -> nodig voor tk.CENTER, nu niet in gebruik
gui = Tk()
gui.geometry("460x350")

s = ttk.Style()
s.theme_names()
s.theme_use('clam')

gui.title("HOAX")

a = ttk.Button(gui, text="LOGIN")
a.grid(row=2, column=0, padx=10, pady=5)

b = ttk.Button(gui, text="CREATE ACCOUNT")
b.grid(row=6, column=0, padx=10, pady=5)

positionRight = int(gui.winfo_screenwidth() / 2 - gui.winfo_reqwidth() / 2)
positionDown = int(gui.winfo_screenheight() / 3 - gui.winfo_reqheight() / 2)

# Positions the window in the center of the page.
gui.geometry("+{}+{}".format(positionRight, positionDown))


gui.mainloop()