import tkinter as tk

class form_pack:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Form")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        fm = tk.Frame(self.master, height = 200, width=400, bg="#87f542")
        fm.pack()

        fm = tk.Frame(self.master, height = 200, width=400, bg="#42adf5")
        fm.pack()


class form_grid:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Form")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        fm = tk.Frame(self.master, height = 100, width=100, bg="#87f542")
        fm.grid(row=0, column=0, padx=10, pady=10) # <- External Padding

        fm = tk.Frame(self.master, height = 100, width=100, bg="#42adf5")
        fm.grid(row=0, column=1, ipadx=10, ipady=10) # <- Internal Padding
        
        fm = tk.Frame(self.master, height = 100, width=100, bg="#87f542")
        fm.grid(row=0, column=2)

        fm = tk.Frame(self.master, height = 100, width=100, bg="#42adf5")
        fm.grid(row=1, column=0)

        fm = tk.Frame(self.master, height = 100, width=100, bg="#87f542")
        fm.grid(row=1, column=1, columnspan=2)

class form_btn:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Form")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        btn1 = tk.Button(self.master, text="Button 1", command=self.method)
        btn1.grid(row=0, column=0)

        btn2 = tk.Button(self.master, text="Button 2", command=lambda : self.method("Some String Arg..."))
        btn2.grid(row=0, column=1)

    def method(self, arg = ""):
        print("Button 1 Pressed", arg)


class form_label:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Form")
        self.master.geometry("100x100")
        self.master.resizable(False, False)

        label1 = tk.Label(self.master, text="Hello World!", fg="red")
        label1.grid(row=0, column=0)

class form_input:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Form")
        self.master.geometry("300x100")
        self.master.resizable(False, False)

        label1 = tk.Label(self.master, text="Enter your name: ", fg="red")
        label1.grid(row=0, column=0)

        text_input = tk.Entry(self.master)
        text_input.grid(row=0, column=1)

        btn = tk.Button(self.master, text="Submit", command=lambda : self.method(text_input.get()))
        btn.grid(row=1, column=0)

    def method(self, arg):
        print("Hello", arg)

def main():
    root = tk.Tk()
    # form_pack(root)

    # form_grid(root)

    # form_btn(root)

    # form_label(root)

    form_input(root)

    root.mainloop()
    pass

if __name__ == "__main__":
    main()