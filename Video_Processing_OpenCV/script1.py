import cv2

def new_size(size, factor):
    size1 = int(size[0] * factor)
    size2 = int(size[1] * factor)
    return (size2, size1)




img = cv2.imread('Video_Processing_OpenCV/galaxy.jpg',0)



resized_image = cv2.resize(img, new_size(img.shape, 0.7))

cv2.imshow('Galaxy', resized_image)
cv2.imwrite('Video_Processing_OpenCV/galaxy_resized.jpg', resized_image)
cv2.waitKey(2000)
cv2.destroyAllWindows()
