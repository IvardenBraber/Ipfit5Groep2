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
import VerifyImageV1
import ExportFilesWindowV1

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
        self.evidence.add_command(label="Verify Image...", command=lambda: VerifyImageV1.Verify())

        self.options = Menu(menubar, tearoff=0)
        self.options.add_command(label="Logout...", command=lambda: [LogoutV1.Logout(), self.destroy()])

        self.help = Menu(menubar, tearoff=0)
        self.help.add_command(label="About...", command=lambda: AboutV1.About())

        self.menuBar.add_cascade(label="Case", menu=self.case)
        self.menuBar.add_cascade(label="Evidence", menu=self.evidence)
        self.menuBar.add_cascade(label="Options", menu=self.options)
        self.menuBar.add_cascade(label="Help", menu=self.help)

        ##aanpassingen
        gridWindow = PanedWindow(self, orient=HORIZONTAL)
        gridWindow.pack(fill=BOTH, expand=True)
        """
        Every column and row has a "weight" grid option associated with it, 
        which tells it how much it should grow if there is extra room in the 
        _F_Cassa to fill. By default, the weight of each column or row is 0, 
        meaning don't expand to fill space.
        """
        gridWindow.grid_rowconfigure(0, weight=1)
        gridWindow.grid_columnconfigure(0, weight=1)

        # I set background colors just to highlight the results
        rightPane = Frame(gridWindow, bg="dark grey")
        leftPane = Frame(gridWindow)

        gridWindow.add(leftPane)
        gridWindow.add(rightPane)

        rightPane.grid(row=0, column=1)
        leftPane.grid(row=0, column=0)

        leftLabel = Label(leftPane, text="Exported files")
        leftLabel.grid(row=0, column=10)

        rightButton = Button(rightPane, text="Export files with hash warnings", command=lambda: ExportFilesWindowV1.Export())
        rightButton.grid(row=0, column=100)

        rightLabel = Label(rightPane, text="Hash Warnings", bg="dark grey")
        rightLabel.grid(row=0, column=0)

        # Resize frame widgets:
        gridWindow.paneconfig(leftPane, width=120, height=400, sticky=E + W + S + N)
        gridWindow.paneconfig(rightPane, width=200, height=400, sticky=E + W + S + N)


    def __init__(self):
        Tk.__init__(self)
        self.widgetsdesign()
        self.config(menu=self.menuBar)


#main hoeft hier niet aangeroepen te worden om te runnen?
if __name__ == "__main__":
    run = Homepage()
    run.title("HOAX")
    run.mainloop()
