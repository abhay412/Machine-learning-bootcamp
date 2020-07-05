from tkinter import *
import tkinter as tk
from first_window import LogIn_Screen

def main():
    root = tk.Tk()
    root.geometry("400x400")
    root.title("Main Window")

    ls = LogIn_Screen(root)
    # f1 = Frame(root, bg = 'cyan', height= 100, width=100)
    # f1.pack()

    root.mainloop()


if __name__ == "__main__":
    main()