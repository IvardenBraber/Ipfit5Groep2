from tkinter import *
from tkinter import ttk
from case import case

#import NewCaseV2
import AboutV1
import LogoutV1
import CloseCaseV1
#import AddImageV1
import OpenCaseV1
import AddImageV2
import NewCaseV3

class Homepage(Tk):

    def widgetsdesign(self):

        self.geometry('700x555')
        self.title('HOAX')

        menubar = Menu(self)
        self.menuBar = Menu(master=self)
        self.case = Menu(self.menuBar, tearoff=0)
        self.case.add_command(label="New Case...", command=lambda: NewCaseV3.NewCase())
        # command=lambda: newCase.createNewCase(self))  # add commands!

        self.case.add_command(label="Open Existing Case...", command=lambda: OpenCaseV1.OpenCase())
        self.case.add_command(label="Close Case...", command=lambda: [self.destroy, CloseCaseV1.CloseCase()])

        self.evidence = Menu(menubar, tearoff=0)
        self.evidence.add_command(label="Add Image...", command=lambda: AddImageV2.AddImage())
        self.evidence.add_command(label="Verify Image...")

        self.options = Menu(menubar, tearoff=0)
        self.options.add_command(label="Logout...", command=lambda: [LogoutV1.Logout(), self.destroy()])

        self.help = Menu(menubar, tearoff=0)
        self.help.add_command(label="About...", command=lambda: AboutV1.About())

        self.menuBar.add_cascade(label="Case", menu=self.case)
        self.menuBar.add_cascade(label="Evidence", menu=self.evidence)
        self.menuBar.add_cascade(label="Options", menu=self.options)
        self.menuBar.add_cascade(label="Help", menu=self.help)

    def __init__(self):
        Tk.__init__(self)
        self.widgetsdesign()
        self.config(menu=self.menuBar)


#main hoeft hier niet aangeroepen te worden om te runnen?
# if __name__ == "__main__":
#     run = homepage()
#     run.title("HOAX")
#     run.mainloop()
