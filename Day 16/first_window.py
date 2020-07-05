from tkinter import *
import tkinter as tk
from alert_window  import AlertBox

class LogIn_Screen(Frame):
    def __init__(self, parent):
        self._parent = parent
        super().__init__(self._parent)

        self.email_text = StringVar()

        email = Entry(self._parent, textvariable = self.email_text)
        email.pack()

        btn = Button(self._parent, text = "Submit", command = self.callBack)
        btn.pack()

    def callBack(self):
        if self.email_text.get() == "":
            ab = AlertBox("This is an ALert!")
        else:
            print(self.email_text.get())
    
    pass