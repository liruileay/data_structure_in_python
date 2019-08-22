########     四个不同的滤波器    #########
import cv2

img = cv2.imread('cat.jpg')

# 均值滤波
img_mean = cv2.blur(img, (5, 5))

# 高斯滤波
img_Guassian = cv2.GaussianBlur(img, (5, 5), 0)

# 中值滤波
img_median = cv2.medianBlur(img, 5)

# 双边滤波
img_bilater = cv2.bilateralFilter(img, 9, 75, 75)

width, height = img.shape[:2][::-1]
img_resize = cv2.resize(img,
                        (int(width * 0.5), int(height * 0.5)), interpolation = cv2.INTER_CUBIC)
# 将图片转为灰度图
img_gray = cv2.cvtColor(img_resize, cv2.COLOR_RGB2GRAY)

#二值化
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)