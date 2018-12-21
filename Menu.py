from tkinter import *

window = Tk()
window.geometry("500x500")

menubar = Menu(window)
case = Menu(menubar, tearoff=0)
case.add_command(label="New Case...") #add commands!
case.add_command(label="Open Existing Case...")
case.add_command(label="Close Case...")

evidence = Menu(menubar, tearoff=0)
evidence.add_command(label="Add Image...")
evidence.add_command(label="Verify Image...")

options = Menu(menubar, tearoff=0)
options.add_command(label="Logout...")

help = Menu(menubar, tearoff=0)
help.add_command(label="About...")

menubar.add_cascade(label="Case", menu=case)
menubar.add_cascade(label="Evidence", menu=evidence)
menubar.add_cascade(label="Options", menu=options)
menubar.add_cascade(label="Help", menu=help)

window.config(menu=menubar)
window.mainloop()
