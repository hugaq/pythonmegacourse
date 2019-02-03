import cv2

image = cv2.imread('smallgray.png', 0)
print(image)
image[0,0] = 255
print(image)
cv2.imwrite('newsmallgrey.png', image)
