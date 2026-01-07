import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('opencv_logo.png', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


kernel = np.ones((5, 5), np.float32) / 25
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5, 5))
gauss_blur = cv2.GaussianBlur(img, (5, 5), 0)
median_blur = cv2.medianBlur(img, 5)
bilater_blur = cv2.bilateralFilter(img, 9, 75, 75)




titles = ['image', '2D-CONVOLUTION', 'blur', 'gaussian_blur', 'median_blur', 'bilater_blur']
images = [img, dst, blur, gauss_blur, median_blur, bilater_blur]

for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])


plt.show()
