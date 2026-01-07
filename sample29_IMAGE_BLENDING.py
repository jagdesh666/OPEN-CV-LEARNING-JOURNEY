import numpy as np
import cv2


apple = cv2.imread('apple.jpg', 1)
orange = cv2.imread('orange.jpg', 1)
orange = cv2.resize(orange, (612, 612))
apple = cv2.resize(apple, (612, 612))

print(apple.shape)
print(orange.shape)


apple_orange = np.hstack((apple[:, :306], orange[:, 306:]))

cv2.imshow("apple_orange", apple_orange)


apple_copy = apple.copy()
gaussian_pyramid_for_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gaussian_pyramid_for_apple.append(apple_copy)


orange_copy = orange.copy()
gaussian_pyramid_for_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gaussian_pyramid_for_orange.append(orange_copy)


laplacian_pyramid_for_apple = [gaussian_pyramid_for_apple[-1]]
for i in range(6, 0, -1):
    size = (gaussian_pyramid_for_apple[i - 1].shape[1], gaussian_pyramid_for_apple[i - 1].shape[0])
    laplacian_expanded = cv2.pyrUp(gaussian_pyramid_for_apple[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid_for_apple[i - 1], laplacian_expanded)
    laplacian_pyramid_for_apple.append(laplacian)


laplacian_pyramid_for_orange = [gaussian_pyramid_for_orange[-1]]
for i in range(6, 0, -1):
    size = (gaussian_pyramid_for_orange[i - 1].shape[1], gaussian_pyramid_for_orange[i - 1].shape[0])
    laplacian_expanded = cv2.pyrUp(gaussian_pyramid_for_orange[i], dstsize=size)
    laplacian = cv2.subtract(gaussian_pyramid_for_orange[i - 1], laplacian_expanded)
    laplacian_pyramid_for_orange.append(laplacian)

apple_orange_pyramid = []
for lap_apple, lap_orange in zip(laplacian_pyramid_for_apple, laplacian_pyramid_for_orange):
    cols = lap_apple.shape[1]
    blended = np.hstack((lap_apple[:, :cols // 2], lap_orange[:, cols // 2:]))
    apple_orange_pyramid.append(blended)


apple_orange_reconstructed = apple_orange_pyramid[0]
for i in range(1, len(apple_orange_pyramid)):
    size = (apple_orange_pyramid[i].shape[1], apple_orange_pyramid[i].shape[0])
    apple_orange_reconstructed = cv2.pyrUp(apple_orange_reconstructed, dstsize=size)
    apple_orange_reconstructed = cv2.add(apple_orange_pyramid[i], apple_orange_reconstructed)


cv2.imshow('apple', apple)
cv2.imshow('orange', orange)
cv2.imshow('simple stack', apple_orange)
cv2.imshow('blended result', apple_orange_reconstructed)

cv2.waitKey(0)
cv2.destroyAllWindows()
