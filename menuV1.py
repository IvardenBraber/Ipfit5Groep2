from tkinter import *
from tkinter import ttk
from case import case

#import different classes
import AboutV1
import LogoutV1
import CloseCaseV1
import OpenCaseV1
import AddImageV2
import NewCaseV3
import VerifyImageV1
import ExportFilesWindowV1


class Homepage(Tk):

    def widgetsdesign(self):

        self.geometry('700x555')
        self.title('HOAX')

        #add menubar to the window and configure it
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

        #make sure all's added to the menuBar to work
        self.menuBar.add_cascade(label="Case", menu=self.case)
        self.menuBar.add_cascade(label="Evidence", menu=self.evidence)
        self.menuBar.add_cascade(label="Options", menu=self.options)
        self.menuBar.add_cascade(label="Help", menu=self.help)

        #aanpassingen

        #grid pane configuraration
        grid_window = PanedWindow(self, orient=HORIZONTAL)
        grid_window.pack(fill=BOTH, expand=True)

        grid_window.grid_rowconfigure(0, weight=1)
        grid_window.grid_columnconfigure(0, weight=1)

        right_pane = Frame(grid_window, bg="grey97")
        left_pane = Frame(grid_window)

        grid_window.add(left_pane)
        grid_window.add(right_pane)

        #positions of the panes
        right_pane.grid(row=0, column=1)
        left_pane.grid(row=0, column=0)

        #adding the export label
        left_label = Label(left_pane, text="Exported files")
        left_label.grid(row=0, column=10)

        #adding the export button
        right_button = Button(right_pane, text="Export files with hash warnings",
                              command=lambda: ExportFilesWindowV1.Export())
        right_button.grid(row=0, column=100)

        #adding the warning label
        right_label = Label(right_pane, text="Hash Warnings", bg="grey97")
        right_label.grid(row=0, column=0)

        #resizing the frame widgets
        grid_window.paneconfig(left_pane, width=120, height=400, sticky=E + W + S + N)
        grid_window.paneconfig(right_pane, width=200, height=400, sticky=E + W + S + N)

    def __init__(self):
        Tk.__init__(self)
        self.widgetsdesign()
        self.config(menu=self.menuBar)


#main hoeft hier niet aangeroepen te worden om te runnen?
if __name__ == "__main__":
    run = Homepage()
    run.title("HOAX")
    run.mainloop()
