from tkinter import *
from tkinter import ttk

#from case import case

import menuV1
import P2
import OpenCaseV1

class CloseCase(Tk):

    def closecasewindow(self):
        gui = self
        gui.geometry("400x250")
        gui.title("HOAX")
        gui.iconbitmap('Hoax.ico')

        close_label = Label(gui, text="Close Case", width=10, font=("bold", 15))
        close_label.place(x=148, y=40)

        a = Label(gui, text="Are you sure you want to close this case?", width=41)
        a.place(x=60, y=110)

        b = ttk.Button(gui, text="YES", width=10, command=lambda: [setZero(), self.destroy()])
            #[P2.HOAX(self.geometry("500x500")), self.destroy()]) #geometry niet werkend
        b.place(x=205, y=175)

        def setZero():
            OpenCaseV1.caseId = 0
            menuV1.Homepage()

        c = ttk.Button(gui, text="NO", width=10, command=self.destroy)
        c.place(x=120, y=175)

    def __init__(self):
        Tk.__init__(self)
        self.closecasewindow()


if __name__ == "__main__":
    run = CloseCase()
    run.title("HOAX")
    run.mainloop()
