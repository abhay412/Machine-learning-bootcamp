import cv2
import numpy as np

v_per = 0.0
h_per = 0.0

def perspective(frame):
    rows, cols = frame.shape[:2]
    corner_points = np.float32([[0,0], [cols-1, 0], [0, rows-1], [cols-1, rows-1]])

    if v_per >= 0:
        v_per_points = np.float32([[cols*v_per, 0], [cols*(1-v_per), 0], [0, rows], [cols, rows]])
    else:
        v_per_points = np.float32([[0, 0], [cols, 0], [cols*(-v_per), rows], [cols*(1+v_per), rows]])
    
    if h_per >= 0:
        h_per_points = np.float32([[0, 0], [cols, rows*(h_per)], [0, rows], [cols, rows*(1-h_per)]])
    else:
        h_per_points = np.float32([[0, rows*(-h_per)], [cols, 0], [0, rows*(1+h_per)], [cols, rows]])


    transform_matrix_v = cv2.getPerspectiveTransform(corner_points, h_per_points)
    transform_matrix_h = cv2.getPerspectiveTransform(corner_points, v_per_points)
    frame = cv2.warpPerspective(frame, transform_matrix_v, (cols, rows))
    frame = cv2.warpPerspective(frame, transform_matrix_h, (cols, rows))
    return frame


cam = cv2.VideoCapture(0)
img_counter = 0

while True:
    ret, frame = cam.read()
    if not ret:
        break

    k = cv2.waitKeyEx(1)

    if k == 2490368:
        # UP Arrow pressed
        v_per += 0.1 if v_per < 0.4 else 0
    elif k == 2621440:
        # DOWN Arrow pressed
        v_per -= 0.1 if v_per > -0.4 else 0
    elif k == 2555904:
        # RIGHT Arrow pressed
        h_per += 0.1 if h_per < 0.4 else 0
    elif k == 2424832:
        h_per -= 0.1 if h_per > -0.4 else 0

    elif k == 27:
        # ESC pressed
        break
    elif k == 32:
        # SPACE pressed
        img_name = "opencv_frame_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

    cv2.imshow("CAM 0", perspective(frame))

cam.release()
cv2.destroyAllWindows()