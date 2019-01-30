from tkinter import *
from tkinter import ttk
#from case import case

# os import
import os
import time

# import different classes
import AboutV1
import LogoutV1
import CloseCaseV1
import OpenCaseV1
import AddImageV2
import NewCaseV3
import VerifyImageV1
import ExportFilesWindowV1
import bookmarkV1
import SeeBookmarksV1
import AddImageV2
from database_nieuw import DatabaseManager



class Homepage(Tk):

    def widgetsdesign(self):

        self.geometry('700x555')
        self.title('HOAX')
        self.iconbitmap('Hoax.ico')
        self.attributes("-topmost", True)
        self.after_idle(self.attributes, '-topmost', False)

        # add menubar to the window and configure it
        menubar = Menu(self)
        self.menuBar = Menu(master=self)
        self.case = Menu(self.menuBar, tearoff=0)
        self.case.add_command(label="New Case...", command=lambda: [self.destroy(), NewCaseV3.NewCase()])
        # command=lambda: newCase.createNewCase(self))  # add commands!

        self.case.add_command(label="Open Existing Case...", command=lambda: [self.destroy(), OpenCaseV1.OpenCase()])
        self.case.add_command(label="Close Case...", command=lambda: [self.destroy(), CloseCaseV1.CloseCase()])

        self.evidence = Menu(menubar, tearoff=0)
        self.evidence.add_command(label="Add Image...", command=lambda: [self.destroy(), AddImageV2.AddImage()])
        self.evidence.add_command(label="Verify Image...", command=lambda: VerifyImageV1.Verify())

        self.options = Menu(menubar, tearoff=0)
        self.options.add_command(label="Bookmarks...", command=lambda: SeeBookmarksV1.Bookmark())
        self.options.add_command(label="Export all Warnings...", command=lambda: ExportFilesWindowV1.Export())
        self.options.add_command(label="Log out...", command=lambda: [self.destroy(), LogoutV1.Logout()])

        self.help = Menu(menubar, tearoff=0)
        self.help.add_command(label="About...", command=lambda: AboutV1.About())

        # make sure all's added to the menuBar to work
        self.menuBar.add_cascade(label="Case", menu=self.case)
        self.menuBar.add_cascade(label="Evidence", menu=self.evidence)
        self.menuBar.add_cascade(label="Options", menu=self.options)
        self.menuBar.add_cascade(label="Help", menu=self.help)

        # aanpassingen

        # grid pane configuraration
        grid_window = PanedWindow(self, orient=HORIZONTAL)
        grid_window.pack(fill=BOTH, expand=True)
        #
        grid_window.grid_rowconfigure(0, weight=1)
        grid_window.grid_columnconfigure(0, weight=1)
        #
        right_pane = Frame(grid_window, bg="grey97")
        left_pane = Frame(grid_window)
        #
        grid_window.add(left_pane)
        grid_window.add(right_pane)
        #
        # # positions of the panes
        right_pane.grid(row=0, column=1)
        left_pane.grid(row=0, column=0)
        #
        # # adding the export label

        print(DatabaseManager.getCaseFolder(DatabaseManager, OpenCaseV1.caseId))

        if OpenCaseV1.caseId == 0 or DatabaseManager.getCaseFolder(DatabaseManager, OpenCaseV1.caseId) == False:
            case_naam = 'No case...'
        else:
            case_naam = DatabaseManager.getCaseFolder(DatabaseManager, OpenCaseV1.caseId)

        #current_user = DatabaseManager.getUserName(DatabaseManager, 1)


        print(case_naam)
        left_label = Label(left_pane, text="Case Name: "+case_naam)
        left_label.grid(row=0, column=10)

        left_label2 = Label(left_pane, text="User: ")
        left_label2.grid(row=1, column=10)
        #
        # # adding the export button
        #right_button = Button(right_pane, text="Export ALL files with hash warnings"
        #                      , command=lambda: ExportFilesWindowV1.Export())
        #right_button.grid(row=0, column=100)
        #
        # # adding the warning label
        right_label = Label(right_pane, text="Hash Warnings", bg="grey97")
        right_label.grid(row=0, column=0)
        #
        # # resizing the frame widgets
        grid_window.paneconfig(left_pane, width=120, height=400, sticky=E + W + S + N)
        grid_window.paneconfig(right_pane, width=200, height=400, sticky=E + W + S + N)
        #
        # # creating an configuring tree view

        path = os.path.basename("C:")



        def klik(event):

            print(AddImageV2.image_list,'\n', AddImageV2.image_loaded)

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


        #filename = os.path.basename("C:\\Users\\aliso\\Downloads\\PBS100%.png")

        #frame = Frame(right_pane)
        #frame.grid(row=0, column=0)

        listbox = Listbox(right_pane, width=75)

        if AddImageV2.image_loaded == False:
            list = ['Test niks ofzo']

            for item in list:
                listbox.insert(END, item)

        if AddImageV2.image_loaded is True:

            list = AddImageV2.image_list #AddImageV2.image_list

            for item in list:
                listbox.insert(END, item)




        #for item in list:
        #    listbox.insert(END, item)

        listbox.place(x=25, y=100)
        listbox.bind("<Double-1>", klik)



    def __init__(self):
        Tk.__init__(self)
        self.widgetsdesign()
        self.config(menu=self.menuBar)


# main hoeft hier niet aangeroepen te worden om te runnen?
#if __name__ == "__main__":
#    run = Homepage()
#    run.title("HOAX")
#    run.mainloop()
