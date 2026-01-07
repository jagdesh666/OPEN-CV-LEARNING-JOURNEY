import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('image4.png', 1)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


lap_lacian = cv2.Laplacian(img, cv2.CV_64F, ksize=5)
lap_lacian = np.uint8(np.absolute(lap_lacian))

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1)
sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

sobel_X_y = np.bitwise_or(sobelx, sobely)
sobel_X_y = np.uint8(np.absolute(sobel_X_y))

canny = cv2.Canny(img, 100, 200)


titles = ['original image', 'laplacian', 'sobelx', 'sobely', 'sobel_x_y', 'canny']
images = [img, lap_lacian, sobelx, sobely, sobel_X_y, canny]


for i in range(6):
    plt.subplot(2, 3, i + 1)
    plt.title(titles[i])
    plt.imshow(images[i])
    plt.xticks([]), plt.yticks([])

plt.show()
