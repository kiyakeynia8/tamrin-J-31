import numpy as np
import cv2

image = cv2.imread("input/Capture.PNG",0)
rows, cols = image.shape
result = np.zeros((rows,cols))

mask = np.array([[-1, 0, 1],
                 [-1, 0, 1],
                 [-1, 0, 1]])

rows, cols = image.shape

for i in range(1, rows-1):
    for j in range(1, cols-1):
        small_img = image[i-1:i+2 , j-1:j+2]
        result[i, j] = np.sum(small_img * mask)

cv2.imwrite("output assignment_31/f_result_4.png",result)