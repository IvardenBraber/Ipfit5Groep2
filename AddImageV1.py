from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from case import case

import menuV1

def browsefunction(self):
    filedirectory = filedialog.askdirectory()
    self.directorypath.set(filedirectory)


class AddImage(Tk):

    def addimagewindow(self):
        gui = self
        gui.geometry("400x250")
        gui.title("HOAX")

        new_case_label = Label(gui, text="Add an Image", width=12, font=("bold", 15))
        new_case_label.place(x=130, y=53)

        a = Label(gui, text="Case Location:", width=15)
        a.place(x=15, y=120)

        ac = Button(gui, text="Browse..", command=lambda: browsefunction(self))
        ac.place(x=274, y=116)

        self.directorypath = StringVar()
        ab = Entry(gui, textvariable=self.directorypath)
        ab.place(x=136, y=120)

        b = ttk.Button(gui, text="Add Image", width=11,
                       command=lambda:  self.destroy())
        b.place(x=195, y=165)

        c = ttk.Button(gui, text="Go Back", width=7, command=self.destroy)
        c.place(x=120, y=165)

    def __init__(self):
        Tk.__init__(self)
        self.addimagewindow()


if __name__ == "__main__":
    run = AddImage()
    run.title("HOAX")
    run.mainloop()
