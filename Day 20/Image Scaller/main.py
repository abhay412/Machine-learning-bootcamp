from tkinter import *
from tkinter import filedialog
from cv_api import Image_Scale

class Scaller(Frame):
    def __init__(self, parent_frame):
        self._master = parent_frame
        super().__init__(self._master)
        self._master.geometry("400x400")
        self.scaleUP_factors = (1, 1)
        self.scaleDown_factors = (1, 1)

        self.fileName = None

        self.initUI()


    def initUI(self):
        button1 = Button(self._master,
                         text = "Select File",
                         command = self.chooseFile)
        button1.pack()

        upBtn = Button(self._master,
                       text="Scale Up")

    def chooseFile(self):
        self.fileName = filedialog.askopenfilename(initialdir = "/",
                                                   title = "Select file",
                                                   filetypes = (("jpeg files","*.jpg"),("all files","*.*"))
                                                   )
        print((self.fileName))


def main():
    root = Tk()
    s = Scaller(root)
    root.mainloop()


if __name__ == '__main__':
    main()