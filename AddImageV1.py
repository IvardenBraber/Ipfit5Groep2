from tkinter import *
from tkinter import ttk
from case import case

import menuV1

class addImage(Tk):


    def addImageWindow(self):
        gui = self
        gui.geometry("600x550")

        newCase_label = Label(gui, text="Add an Image", width=12, font=("bold", 15))
        newCase_label.place(x=170, y=53)


        e = ttk.Button(gui, text="Add Image", width=11,
                       command= lambda: menuV1.homepage())
        e.place(x=195, y=430)

        f = ttk.Button(gui, text="Go Back", width=7, command= self.destroy)
        f.place(x=120, y=430)

    def __init__(self):
        Tk.__init__(self)
        self.addImageWindow()

if __name__ == "__main__":
    run = addImage()
    run.title("HOAX")
    run.mainloop()

