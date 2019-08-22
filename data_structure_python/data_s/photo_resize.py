import cv2

image = cv2.imread("1.jpg")
new_image = cv2.resize(image,(358,441))
cv2.imwrite("2.jpg",new_image)