import cv2
import numpy as np

def rotate_CW(file):
    img = cv2.imread(file)
    num_rows, num_cols = img.shape[:2]
    rot_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), -10, 1)
    img_2 = cv2.warpAffine(img, rot_matrix, (num_cols, num_rows))
    cv2.imwrite(file, img_2)

def rotate_counterCW(file):
    img = cv2.imread(file)
    num_rows, num_cols = img.shape[:2]
    rot_matrix = cv2.getRotationMatrix2D((num_cols / 2, num_rows / 2), 10, 1)
    img_2 = cv2.warpAffine(img, rot_matrix, (num_cols, num_rows))
    cv2.imwrite(file, img_2)