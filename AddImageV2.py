from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from case import case

import menuV1

def browsefunction(self):
    file = filedialog.askopenfilename()
    self.directorypath.set(file)


class AddImage(Tk):

    def addimagewindow(self):
        gui = self
        gui.geometry("600x425")
        gui.title("HOAX")

        new_case_label = Label(gui, text="Add an Image", width=12, font=("bold", 15))
        new_case_label.place(x=230, y=53)

        g = Label(gui, text="Image number: ", width=14)
        g.place(x=111, y=120)

        gb = Entry(gui)
        gb.place(x=236, y=120)

        imagenumber = gb.get()

        a = Label(gui, text="Image Location:", width=15)
        a.place(x=108, y=170)

        ac = Button(gui, text="Browse..", command=lambda: browsefunction(self))
        ac.place(x=372, y=166)

        self.directorypath = StringVar()
        ab = Entry(gui, textvariable=self.directorypath)
        ab.place(x=236, y=170)

        imagepath = ab.get()

        b = Label(gui, text="Serial number: ", width=15)
        b.place(x=104, y=220)

        bb = Entry(gui)
        bb.place(x=236, y=220)

        h = Label(gui, text="Data carrier number: ", width=21)
        h.place(x=98, y=270)

        hb = Entry(gui)
        hb.place(x=236, y=270)

        b = ttk.Button(gui, text="Add Image", width=11,
                       command=lambda:  self.destroy())
        b.place(x=295, y=345)

        c = ttk.Button(gui, text="Go Back", width=7, command=self.destroy)
        c.place(x=220, y=345)

    def __init__(self):
        Tk.__init__(self)
        self.addimagewindow()


if __name__ == "__main__":
    run = AddImage()
    run.title("HOAX")
    run.mainloop()
