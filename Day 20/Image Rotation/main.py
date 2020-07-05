from tkinter import *
from tkinter import filedialog
import cv2

def rotate_CW(file, degree):
    img_backup = cv2.imread(file)
    img = img_backup
    cv2.imwrite("e:\img.jpg", img_backup)

    num_rows, num_cols = img.shape[:2]
    rot_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), degree, 1)
    img_2 = cv2.warpAffine(img, rot_matrix, (num_cols, num_rows))
    cv2.imwrite(file, img_2)



def plusBtn_Event(file):
    cv_api.rotate_counterCW(file)

def minusBtn_Event(file):
    cv_api.rotate_CW(file)

def main():
    root = Tk()
    root.geometry("400x400")

    label1 = Label(root, text="Enter a image location here")
    label1.pack()

    # filePath = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("png files","*."),("all files","*.*")))

    entry1 = Entry(root)
    entry1.pack()

    button1 = Button(root, text="+", command=lambda :plusBtn_Event(entry1.get()))
    button1.pack()

    button2 = Button(root, text="-", command=lambda :minusBtn_Event(entry1.get()))
    button2.pack()

    root.mainloop()

if __name__ == '__main__':
    main()