import cv2
import numpy as np

image = cv2.imread('input/flower_input.jpg',0)

filter = np.ones((19, 19),np.float32)/361

x, y = image.shape
for i in range(9, x - 9):
    for j in range(9, y - 9):
        if 0 < image[i, j] < 50:
            sml = image[i-9:i+10, j-9:j+10]
            image[i, j] = np.sum(sml * filter)

cv2.imwrite('output assignment_31/f_result_2.png', image)