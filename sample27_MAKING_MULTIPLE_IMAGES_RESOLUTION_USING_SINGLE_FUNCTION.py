import cv2

img = cv2.imread('image1.jpg')

layer = img.copy()
gaussian_parameter = [layer]

for i in range(5):
    layer = cv2.pyrDown(layer)
    gaussian_parameter.append(layer)
    cv2.imshow(str(i + 1), layer)


layer = gaussian_parameter[-1]
laplacian_parameter = [layer]

for i in range(5, 0, -1):
    layer = cv2.pyrUp(layer)
    layer = cv2.resize(layer, (gaussian_parameter[i - 1].shape[1], gaussian_parameter[i - 1].shape[0]))
    laplacian = cv2.subtract(gaussian_parameter[i - 1], layer)
    laplacian_parameter.append(laplacian)
    cv2.imshow(f"Laplacian {i}", laplacian)


cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
