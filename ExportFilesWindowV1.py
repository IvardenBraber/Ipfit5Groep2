from tkinter import *
from tkinter import filedialog

def browsefunction(self):
    filedirectory = filedialog.askdirectory()
    self.directorypath.set(filedirectory)


class Export(Tk):

    def exportfiles(self):
        gui = self
        gui.geometry("500x250")
        gui.title("HOAX")

        export_label = Label(gui, text="Exporting File(s)", width=17, font=("bold", 15))
        export_label.place(x=148, y=43)

        a = Label(gui, text="Destination export file(s): ", width=128)
        a.place(x=-300, y=100)

        c = Button(gui, text="Browse..", command=lambda: browsefunction(self))
        c.place(x=372, y=95)

        self.directorypath = StringVar()
        bb = Entry(gui, textvariable=self.directorypath)
        bb.place(x=236, y=100)

        go_back = Button(gui, text="Go Back", width=7, command=lambda: self.destroy())
        go_back.place(x=110, y=140)

        c = Button(gui, text="Start the exporting proces", width=26)  #, command=lambda: browsefunction(self))
        c.place(x=172, y=140)

    def __init__(self):
        Tk.__init__(self)
        self.exportfiles()


if __name__ == "__main__":
    run = Export()
    run.mainloop()
