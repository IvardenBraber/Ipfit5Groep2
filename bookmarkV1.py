from tkinter import *
from tkinter import filedialog

import ExportFilesWindowV1
import menuV1


class Bookmark(Tk):

    def bookmarkfiles(self):
        gui = self
        gui.geometry("350x250")
        gui.title("HOAX")

        export_label = Label(gui, text="Bookmark file", width=13, font=("bold", 15))
        export_label.place(x=110, y=43)

        a = Label(gui, text="Are you sure you want to bookmark this file?", width=44)
        a.place(x=20, y=100)

        go_back = Button(gui, text="Go Back", width=7, command=lambda: self.destroy())
        go_back.place(x=70, y=140)

        c = Button(gui, text="Add bookmark", width=16)#, command=lambda: browsefunction(self))
        c.place(x=135, y=140)

    def __init__(self):
        Tk.__init__(self)
        self.bookmarkfiles()


if __name__ == "__main__":
    run = Bookmark()
    run.mainloop()
