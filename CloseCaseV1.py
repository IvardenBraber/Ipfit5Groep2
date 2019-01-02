from tkinter import *
from tkinter import ttk

from case import case

import menuV1
import P2

class closeCase(Tk):

    def closeCaseWindow(self):
        gui = self
        gui.geometry("400x250")
        gui.title("HOAX")

        logout_label = Label(gui, text="Close Case", width=10, font=("bold", 15))
        logout_label.place(x=148, y=40)

        a = Label(gui, text="Are you sure you want to close this case?", width=41)
        a.place(x=60, y=110)

        e = ttk.Button(gui, text="YES", width=10, command= lambda: self.destroy())#[P2.HOAX(self.geometry("500x500")), self.destroy()]) #geometry niet werkend
        e.place(x=205, y=175)

        f = ttk.Button(gui, text="NO", width=10, command= self.destroy)
        f.place(x=120, y=175)

    def __init__(self):
        Tk.__init__(self)
        self.closeCaseWindow()


if __name__ == "__main__":
    run = closeCase()
    run.title("HOAX")
    run.mainloop()