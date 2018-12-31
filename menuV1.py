from tkinter import *
from tkinter import ttk
from case import case

import NewCaseV1
import AboutV1
import LogoutV1
import CloseCaseV1
import AddImageV1

class homepage(Tk):

    def widgetsDesign(self):

        self.geometry('700x555')

        menubar = Menu(self)
        self.menuBar = Menu(master=self)
        self.case = Menu(self.menuBar, tearoff=0)
        self.case.add_command(label="New Case...", command=lambda: NewCaseV1.newCase()) # command=lambda: newCase.createNewCase(self))  # add commands!

        self.case.add_command(label="Open Existing Case...")
        self.case.add_command(label="Close Case...", command=lambda: CloseCaseV1.closeCase())

        self.evidence = Menu(menubar, tearoff=0)
        self.evidence.add_command(label="Add Image...", command= lambda: AddImageV1.addImage())
        self.evidence.add_command(label="Verify Image...")

        self.options = Menu(menubar, tearoff=0)
        self.options.add_command(label="Logout...", command= lambda: LogoutV1.logout())

        self.help = Menu(menubar, tearoff=0)
        self.help.add_command(label="About...", command= lambda: AboutV1.about())

        self.menuBar.add_cascade(label="Case", menu=self.case)
        self.menuBar.add_cascade(label="Evidence", menu=self.evidence)
        self.menuBar.add_cascade(label="Options", menu=self.options)
        self.menuBar.add_cascade(label="Help", menu=self.help)


    def __init__(self):
        Tk.__init__(self)
        self.widgetsDesign()
        self.config(menu=self.menuBar)


if __name__ == "__main__":
    run = homepage()
    run.title("HOAX")
    run.mainloop()