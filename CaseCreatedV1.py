from tkinter import *
from tkinter import ttk
from case import case

import menuV1


class NewClassCreated(Tk):

    def newclasscreated(self):
        gui = self
        gui.geometry("500x250")
        gui.title("HOAX")

        new_case_label = Label(gui, text="New Case", width=14, font=("bold", 15))
        new_case_label.place(x=170, y=53)

        a = Label(gui, text="The new case has been created. You can close this window now.", width=61)
        a.place(x=45, y=130)

    def __init__(self):
        Tk.__init__(self)
        self.newclasscreated()

# if __name__ == "__main__":
#     run = newClassCreated()
#     run.title("HOAX")
#     run.mainloop()
