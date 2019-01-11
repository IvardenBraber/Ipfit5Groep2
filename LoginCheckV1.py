from tkinter import *
import tkinter.messagebox as tm

import P2

class login_check():

    #def __init__(self):
    #    super().__init__(master)

    print("click")
    username = P2.usernameEntry.get()
    password = P2.Login.passwordEntry.get()

    print(username, password)

    self.mainloop()