import Tkinter, ttk

class App(Tkinter.Frame):
    def __init__(self, parent):
        Tkinter.Frame.__init__(self, parent, relief=Tkinter.SUNKEN, bd=2)
        self.parent = parent

        self.menubar = Tkinter.Menu(self)
        self.parent.winfo_toplevel().configure(menu=self.menubar)

        self.tree = ttk.Treeview(self)

        self.yscrollbar = ttk.Scrollbar(self, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.yscrollbar.set)

        self.tree.grid(row=0, column=0, sticky="nsew")
        self.yscrollbar.grid(row=0, column=1, sticky='nse')
        self.yscrollbar.configure(command=self.tree.yview)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

if __name__ == "__main__":
    root = Tkinter.Tk()
    root.title("MyApp")
    app = App(root)
    app.pack(fill="both", expand=True)
    app.mainloop()