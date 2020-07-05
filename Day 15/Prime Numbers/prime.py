import tkinter as tk
from colors import colors
from random import choice

class Prime:

    def __init__(self, master):
        self.height = 300
        self.width = 500

        self.__oldvalue = ""


        w = master.winfo_screenwidth()
        h = master.winfo_screenheight()

        x = (w//2) - (self.width//2)
        y = (h//2) - (self.height//2)

        self.theme_name = 'Blue_Berries'
        self.set_theme()

        master.bind('<t>', self.randomize_theme)


        self.master = master
        self.master.title("Prime Number?")
        self.master.geometry("{}x{}+{}+{}".format(self.width, self.height, x, y))
        self.master.resizable(False, False)

        self.input_frame = tk.Frame(self.master, height=self.height//2, width=self.width, bg=self.col_bg)
        self.input_frame.grid(row=0, column=0)

        self.label_1 = tk.Label(self.input_frame,
                            bg = self.col_bg,
                            fg = self.col_fg,
                            justify = "center",
                            font = "Montserrat 15",
                            text = "Enter your number below")
        self.label_1.place(relx = 0.5, y=10,anchor = "n")

        self.test_number = tk.StringVar()
        self.test_number.trace("w", self.entry_callback)

        self.num_entry = tk.Entry(self.input_frame, 
                             bg=self.col_bg,
                             fg = self.col_fg,
                             width=10,
                             justify="center", 
                             bd=0, font="Montserrat 40 bold", 
                             textvariable=self.test_number
                             )
        self.num_entry.place(relx=0.5, rely=0.4, anchor='n')
        self.num_entry.focus()

        self.output_frame = tk.Frame(self.master, height=self.height//2, width=self.width, bg=self.col_bg)
        self.output_frame.grid(row=1, column=0)

        self.label_2 = tk.Label(self.output_frame,
                            bg = self.col_bg,
                            fg = self.col_fg,
                            justify = "center",
                            font = "Montserrat 45",
                            text = "Umm..."
                            )
        self.label_2.place(relx = 0.5, y=10, anchor = "n")

        self.error_lbl = tk.Label(self.output_frame,
                            bg = self.col_bg,
                            fg = self.col_warning,
                            justify = "center",
                            font = "Montserrat 10",
                            text = "Waiting for a number!"
                            )
        self.error_lbl.place(relx=0.5, y=140,anchor="s")

    def randomize_theme(self, event):
        themes = ['theme1', 'Blue_Berries', 'Lemon']
        themes.remove(self.theme_name)
        
        self.theme_name = choice(themes)
        # print(self.theme_name)
        self.set_theme()
        self.update_ui()


    def set_theme(self):
        self.current_theme = colors[self.theme_name]
        self.col_bg = self.current_theme['bg']
        self.col_fg = self.current_theme['fg']
        self.col_default = self.current_theme['default']
        self.col_not_prime = self.current_theme['not_prime']
        self.col_prime = self.current_theme['prime']
        self.col_warning = self.current_theme['warning']
        
    
    def update_ui(self):
        self.label_1.configure(bg=self.col_bg, fg=self.col_fg)
        self.label_2.configure(bg=self.col_bg, fg=self.col_fg)
        self.error_lbl.configure(bg=self.col_bg, fg=self.col_warning)
        self.num_entry.configure(bg=self.col_bg, fg=self.col_fg)

        self.input_frame.configure(bg=self.col_bg)
        self.output_frame.config(bg=self.col_bg)
        

    def entry_callback(self, *args):
        string = self.test_number.get()
        if len(string) > 10:
            self.test_number.set(self.__oldvalue)
            self.error_lbl['text'] = "Whoa! Hold on, input limit is 10"

        elif string != "" and string.isdigit():
            number = int(string)

            result_string, color = self.check_prime(number)

            self.label_2['text'] = result_string
            self.label_2['fg'] = color
            self.error_lbl['text'] = ""
            self.__oldvalue = string

        elif string == "":
            self.label_2['fg'] = self.col_default
            self.label_2['text'] = "Umm..."
            self.error_lbl['text'] = "Waiting for a number!"
            self.__oldvalue = ""

        elif not string.isdigit():
            if self.__oldvalue == "":
                self.label_2['fg'] = self.col_default
                self.label_2['text'] = "Umm..."
                self.test_number.set("")
            else:
                self.test_number.set(self.__oldvalue)
                number = int(self.__oldvalue)
                result_string, color = self.check_prime(number)
                self.label_2['text'] = result_string
                self.label_2['fg'] = color

            self.error_lbl['text'] = "Opps... Only Integers Please!"

            
    def check_prime(self, num):
        if num > 1:
            if num in [2,3]:
                return ("Prime", self.col_prime)
            for i in range(2, num//2+1):
                if (num % i) == 0:
                    return ("Not Prime", self.col_not_prime)
                    break  
                else:  
                    return ("Prime", self.col_prime)
        else:  
            return ("Not Sure!", self.col_default)


def main():
    root = tk.Tk()
    new_window = Prime(root)
    root.mainloop()
    pass


if __name__ == "__main__":
    main()