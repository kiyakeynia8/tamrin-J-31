import numpy as np 
import cv2

# image = cv2.imread("input/Capture (2).PNG",0)
image = cv2.imread("input/board_noisy.png",0)
rows,cols = image.shape

result = np.zeros((rows,cols))
# filter = np.ones((3,3))/9

# for i in range(1,rows-1):
#     for j in range(1,cols-1):
#         small = img[i-1:i+2,j-1:j+2]
#         average = np.sum(filter*small)
#         result[i,j] = average

filter = np.ones((5,5))/25

for i in range(2,rows-2):
    for j in range(2,cols-2):
        small = image[i-2:i+3,j-2:j+3]
        average = np.sum(filter*small)
        result[i,j] = average

# cv2.imwrite("output assignment_31/f1_result_5.png", result)
cv2.imwrite("output assignment_31/f2_result_5.png", result)