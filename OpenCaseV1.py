from tkinter import *
from tkinter import ttk
from tkinter import filedialog
#from case import case

import menuV1
import CaseCreatedV1


def browsefunction(self):
    filedirectory = filedialog.askdirectory()
    self.directorypath.set(filedirectory)


class OpenCase(Tk):

    def opencase(self):
        gui = self
        gui.geometry("400x250")
        gui.title("HOAX")

        new_case_label = Label(gui, text="Load Case", width=9, font=("bold", 15))
        new_case_label.place(x=148, y=53)

        c = Label(gui, text="Case Location:", width=15)
        c.place(x=15, y=130)

        cc = Button(gui, text="Browse..", command=lambda: browsefunction(self))
        cc.place(x=274, y=126)

        self.directorypath = StringVar()
        cb = Entry(gui, textvariable=self.directorypath)
        cb.place(x=136, y=130)

        e = ttk.Button(gui, text="Open Case", width=11, command=lambda: self.destroy())
        e.place(x=185, y=200)

        f = ttk.Button(gui, text="Go Back", width=7, command=self.destroy)
        f.place(x=125, y=200)

    def __init__(self):
        Tk.__init__(self)
        self.opencase()


if __name__ == "__main__":
    run = OpenCase()
    run.title("HOAX")
    run.mainloop()
