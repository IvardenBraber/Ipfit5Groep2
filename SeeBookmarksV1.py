from tkinter import *
from tkinter import filedialog

import ExportFilesWindowV1
import menuV1
import os

class Bookmark(Tk):

    def bookmarkfiles(self):
        gui = self
        gui.geometry("350x350")
        gui.title("HOAX")

        export_label = Label(gui, text="Bookmarked files", width=13, font=("bold", 16))
        export_label.place(x=110, y=43)

        a = Label(gui, text="blank", width=44)
        a.place(x=20, y=100)

        filename = os.path.basename("E:\\2e jaar Informatica\\Periode 2\\IPFIT5\\code")

        listbox = Listbox(self)
        listbox.insert(END, filename)
        listbox.place(x=120, y=100)


        go_back = Button(gui, text="Go Back", width=14, command=lambda: self.destroy())
        go_back.place(x=125, y=300)


    def __init__(self):
        Tk.__init__(self)
        self.bookmarkfiles()


if __name__ == "__main__":
    run = Bookmark()
    run.mainloop()
