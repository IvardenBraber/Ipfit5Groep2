from tkinter import *
import tkinter as tk


class HOAX(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frame = {}
        for F in (Main, CreateAccount, Login, homepage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frame[page_name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Main")

    def show_frame(self, page_name):
        frame = self.frame[page_name]
        frame.tkraise()

class Main(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        a = Button(self, text="LOGIN", command=lambda: controller.show_frame("Login"))
        a.place(x=220, y=200)

        b = Button(self, text="CREATE ACCOUNT", command=lambda: controller.show_frame("CreateAccount"))
        b.place(x=185, y=250)

class Login(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        login_label = Label(self, text="Login Page", width=14, font=("bold", 15))
        login_label.place(x=170, y=73)

        a = Label(self, text="Username: ")
        a.place(x=130, y=200)

        b = Label(self, text="Password: ")
        b.place(x=132, y=220)

        c = Button(self, text="LOGIN", width=5, command=lambda: controller.show_frame("homepage")) #homepage command toegevoegd
        c.place(x=200, y=350)

        f = Button(self, text="Go Back", width=7, command=lambda: controller.show_frame("Main"))
        f.place(x=120, y=350)

        E = Entry(self)
        E.place(x=220, y=200)
        F = Entry(self, show="**")
        F.place(x=220, y= 220)


class CreateAccount(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        createAccount_label = Label(self, text="Create Account", width=14, font=("bold", 15))
        createAccount_label.place(x=170, y=53)

        a = Label(self, text="Full Name: ", width=11)
        a.place(x=80,y=130)

        ab = Entry(self)
        ab.place(x=185, y=130)

        b = Label(self, text="Email: ", width=7)
        b.place(x=90,y=180)

        bb = Entry(self)
        bb.place(x=185, y=180)

        c = Label(self, text="Username: ", width=10)
        c.place(x=80,y=230)

        cb = Entry(self)
        cb.place(x=185, y= 230)

        d = Label(self, text="Password: ", width=10)
        d.place(x=80,y=280)

        db = Entry(self, show="**")
        db.place(x=185, y=280)

        e = Button(self, text="Register account", width=16)
        e.place(x=195, y=350)

        f = Button(self, text="Go Back", width=7, command=lambda: controller.show_frame("Main"))
        f.place(x=120,y=350)

class homepage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        menubar = Menu(self)
        case = Menu(menubar, tearoff=0)
        case.add_command(label="New Case...")  # add commands!
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

        self.config(menu=menubar)

# class homepage():
#     window = Tk()
#     window.geometry("500x500")
#
#     menubar = Menu(window)
#     case = Menu(menubar, tearoff=0)
#     case.add_command(label="New Case...")  # add commands!
#     case.add_command(label="Open Existing Case...")
#     case.add_command(label="Close Case...")
#
#     evidence = Menu(menubar, tearoff=0)
#     evidence.add_command(label="Add Image...")
#     evidence.add_command(label="Verify Image...")
#
#     options = Menu(menubar, tearoff=0)
#     options.add_command(label="Logout...")
#
#     help = Menu(menubar, tearoff=0)
#     help.add_command(label="About...")
#
#     menubar.add_cascade(label="Case", menu=case)
#     menubar.add_cascade(label="Evidence", menu=evidence)
#     menubar.add_cascade(label="Options", menu=options)
#     menubar.add_cascade(label="Help", menu=help)

    #window.config(menu=menubar)
    #window.mainloop()



#positionRight = int(tk.winfo_screenwidth() / 2 - tk.winfo_reqwidth() / 2)
# positionDown = int(tk.winfo_screenheight() / 3 - tk.winfo_reqheight() / 2)

#tk.geometry("+{}+{}".format(positionRight, positionDown))

if __name__ == '__main__':
    test = HOAX()
    test.geometry("500x500")
    test.mainloop()
