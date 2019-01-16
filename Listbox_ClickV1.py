import tkinter
from tkinter import Tk
from tkinter import *

class klik(Tk):

    def klik(event):
        print("click")
        newwindow = Tk()
        newwindow.title("Window")
        newwindow.geometry("400x350")

        option_title = Label(newwindow, text="Export or Bookmark?", width=19, font=("bold", 15))
        option_title.place(x=100, y=50)

        export_label = Label(newwindow, text="Do you want to export this file?", width=32)
        export_label.place(x=80, y=120)

        export_button = Button(newwindow, text="YES", width=3, command=lambda: ExportFilesWindowV1.Export())
        export_button.place(x=180, y=155)

        bookmark_label = Label(newwindow, text="Do you want to bookmark this file?", width=34)
        bookmark_label.place(x=75, y=220)

        bookmark_button = Button(newwindow, text="YES", width=3, command=lambda: bookmarkV1.Bookmark())
        bookmark_button.place(x=180, y=255)

    def __init__(self):
        Tk.__init__(self)
        self.klik()

if __name__ == "__main__":
    run = klik()
    run.mainloop()