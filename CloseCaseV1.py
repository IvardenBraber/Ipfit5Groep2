from tkinter import *
from tkinter import ttk

from case import case

import menuV1
import P2

class closeCase(Tk):

    def closeCaseWindow(self):
        gui = self
        gui.geometry("600x550")


        logout_label = Label(gui, text="Close Case", width=10, font=("bold", 15))
        logout_label.place(x=170, y=53)

        a = Label(gui, text="Are you sure you want to close this case?", width=41)
        a.place(x=80, y=130)

        e = ttk.Button(gui, text="YES", width=10, command= lambda: P2.HOAX(self.geometry("500x500"))) #geometry niet werkend
        e.place(x=195, y=430)

        f = ttk.Button(gui, text="NO", width=10, command= self.destroy)
        f.place(x=120, y=430)

    def __init__(self):
        Tk.__init__(self)
        self.closeCaseWindow()


if __name__ == "__main__":
    run = closeCase()
    run.title("HOAX")
    run.mainloop()