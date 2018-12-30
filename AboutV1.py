from tkinter import *
from tkinter import ttk
from case import case

import menuV1

class about(Tk):

    def aboutinfo(self):
        gui = self
        gui.geometry("400x250")

        newCase_label = Label(gui, text="About this tool", width=15, font=("bold", 15))
        newCase_label.place(x=170, y=53)

        a = Label(gui, text="", width=10)
        a.place(x=70, y=130)

    def __init__(self):
        Tk.__init__(self)
        self.aboutinfo()
        #self.config(menu=self.menuBar)

if __name__ == "__main__":
    run = about()
    run.mainloop()

