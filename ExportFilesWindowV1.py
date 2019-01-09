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

        new_case_label = Label(gui, text="Exporting File(s)", width=17, font=("bold", 15))
        new_case_label.place(x=148, y=43)

        a = Label(gui, text="Destination export file(s): ", width=128)
        a.place(x=-300, y=100)

        ac = Button(gui, text="Browse..", command=lambda: browsefunction(self))
        ac.place(x=372, y=95)

        self.directorypath = StringVar()
        ab = Entry(gui, textvariable=self.directorypath)
        ab.place(x=236, y=100)

        ac = Button(gui, text="Start the exporting proces", width=26)#, command=lambda: browsefunction(self))
        ac.place(x=152, y=140)


    def __init__(self):
        Tk.__init__(self)
        self.exportfiles()


if __name__ == "__main__":
    run = Export()
    run.mainloop()