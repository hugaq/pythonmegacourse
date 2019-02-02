import cv2

image = cv2.imread('smallgray.png', 0)
image[0,0] = 255
print(image)
cv2.imwrite('newsmallgrey.png', image)
for i in range(image.shape):
    print(i)
