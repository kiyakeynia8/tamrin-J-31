import numpy as np
import cv2

# image = cv2.imread("input\lion.png",0)
image = cv2.imread("input/spider.png",0)
rows, cols = image.shape
result = np.zeros((rows,cols))

filter = np.array([[-1, -1, -1],
                   [-1,  8, -1],
                   [-1, -1, -1]])
                   
for i in range(1,rows-1):
    for j in range(1,cols-1):
        small = image[i-1:i+2, j-1:j+2]
        result[i, j] = np.sum(small * filter)

# cv2.imwrite("output assignment_31/f1_result_3.png",result)
cv2.imwrite("output assignment_31/f2_result_3.png",result)