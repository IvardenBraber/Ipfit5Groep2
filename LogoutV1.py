from tkinter import *
from tkinter import ttk

from case import case

import menuV1
import P2

class logout(Tk):

    def logoutWindow(self):
        gui = self
        gui.geometry("600x550")

        logout_label = Label(gui, text="Logout", width=6, font=("bold", 15))
        logout_label.place(x=170, y=53)

        a = Label(gui, text="Are you sure you want to logout as the current user?", width=64)
        a.place(x=80, y=130)

        e = ttk.Button(gui, text="YES", width=10, command= lambda: menuV1.homepage())
        e.place(x=195, y=430)

        f = ttk.Button(gui, text="NO", width=10, command= self.destroy)
        f.place(x=120, y=430)

    def __init__(self):
        Tk.__init__(self)
        self.logoutWindow()


if __name__ == "__main__":
    run = logout()
    run.title("HOAX")
    run.mainloop()
