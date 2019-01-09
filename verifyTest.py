from tkinter import *
import tkinter as tk


class Listbox(Tk):

    def get_list(event):
        """
        function to read the listbox selection
        and put the result in an entry widget
        """
        # get selected line index
        index = listbox1.curselection()[0]
        # get the line's text
        seltext = listbox1.get(index)
        # delete previous text in enter1
        enter1.delete(0, 50)
        # now display the selected text
        enter1.insert(0, seltext)

    # create the sample data file
    str1 = """imagename
    """
    fout = open("verifyimage.txt", "w")
    fout.write(str1)
    fout.close()

    # read the data file into a list
    fin = open("verifyimage.txt", "r")
    imagename_list = fin.readlines()
    fin.close()
    # strip the trailing newline char
    imagename_list = [imagefile.rstrip() for imagefile in imagename_list]

    root = tk.Tk()
    root.title("Listbox Operations")
    #create the listbox (note that size is in characters)
    listbox1 = tk.Listbox(root, width=50, height=6)
    listbox1.grid(row=0, column=0)

    # create a vertical scrollbar to the right of the listbox
    yscroll = tk.Scrollbar(command=listbox1.yview, orient=tk.VERTICAL)
    yscroll.grid(row=0, column=1, sticky=tk.N + tk.S)
    listbox1.configure(yscrollcommand=yscroll.set)

    # use entry widget to display/edit selection
    enter1 = tk.Entry(root, width=50)
    enter1.insert(0, 'Click on an image file')
    enter1.grid(row=1, column=0)

    # load the listbox with data
    for item in imagename_list:
        listbox1.insert(tk.END, item)

    # left mouse click on a list item to display selection
    listbox1.bind('<ButtonRelease-1>', get_list)

    root.mainloop()