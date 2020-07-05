from tkinter import *
import tkinter as tk

class AlertBox():
    def __init__(self, text):
        self.dialog = tk.Toplevel()
        self.dialog.grab_set()
        label = Label(self.dialog, text=text)
        label.pack()

        ok_btn = Button(self.dialog, text="OK", command=self.ok_event)
        ok_btn.pack()

        self.dialog.mainloop()
        pass

    def ok_event(self):
        self.dialog.grab_release()
        self.dialog.destroy()
        