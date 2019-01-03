from tkinter import *
from tkinter import ttk
from case import case

import menuV1


class AddImage(Tk):

    def addimagewindow(self):
        gui = self
        gui.geometry("600x550")
        gui.title("HOAX")

        new_case_label = Label(gui, text="Add an Image", width=12, font=("bold", 15))
        new_case_label.place(x=170, y=53)

        e = ttk.Button(gui, text="Add Image", width=11,
                       command=lambda: menuV1.Homepage())
        e.place(x=195, y=430)

        f = ttk.Button(gui, text="Go Back", width=7, command=self.destroy)
        f.place(x=120, y=430)

    def __init__(self):
        Tk.__init__(self)
        self.addimagewindow()


if __name__ == "__main__":
    run = addImage()
    run.title("HOAX")
    run.mainloop()
