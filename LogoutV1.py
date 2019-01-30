from tkinter import *
from tkinter import ttk

#from case import case

import menuV1
import P2

from menuV1 import *

def test():
    menuV1.AddImageV2.image_loaded = False


class Logout(Tk):

    def logoutwindow(self):
        gui = self
        gui.geometry("400x250")
        gui.title("HOAX")

        logout_label = Label(gui, text="Log out", width=6, font=("bold", 15))
        logout_label.place(x=160, y=53)

        a = Label(gui, text="Are you sure you want to log out as the current user?", width=64)
        a.place(x=-10, y=110)

        e = ttk.Button(gui, text="YES", width=10, command=lambda: [self.destroy(), test(), P2.HOAX()])#[P2.HOAX(), self.destroy()])
        e.place(x=205, y=175)

        f = ttk.Button(gui, text="NO", width=10, command=lambda: [self.destroy(), menuV1.Homepage()]) #, test(), menuV1.Homepage()]) #, menuV1.Homepage()) #, menuV1.Homepage.delete, menuV1.Homepage()])
        f.place(x=120, y=175)

    def __init__(self):
        Tk.__init__(self)
        self.logoutwindow()


if __name__ == "__main__":
    run = Logout()
    run.title("HOAX")
    run.mainloop()
