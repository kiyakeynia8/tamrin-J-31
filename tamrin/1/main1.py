import matplotlib.pyplot as plt
import cv2

def histogram(image_ad):
    image = cv2.imread(image_ad,0)

    x,y = image.shape
    a = 0

    hist = []
    for i in range(256):
        hist.append(0)

    for i in range(x):
        for j in range(y):
            b = image[i][j]
            hist[b] += 1

    return hist

plt.plot(histogram("input/flower_input.jpg"))
# plt.hist(histogram("input\Capture.PNG"))
plt.show()