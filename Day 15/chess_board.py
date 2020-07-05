import tkinter as tk


class form_grid:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Form")
        self.master.geometry("400x400")
        self.master.resizable(False, False)

        for i in range(8):
            for j in range(8):
                color = "#000000" if i%2 else "#ffffff"
                box = tk.Frame(self.master, height = 100, width=100, bg=color)
                box.grid(row=i, column=j)

def main():
    root = tk.Tk()

    form_grid(root)

    root.mainloop()
    pass

if __name__ == "__main__":
    main()