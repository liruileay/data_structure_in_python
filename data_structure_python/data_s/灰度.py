import cv2
import numpy as np


img_path = "timg.jpg"
img = cv2.imread(img_path)
# 获取图片的宽和高
width, height = img.shape[:2][::-1]
# 将图片缩小便于显示观看
img_resize = cv2.resize(img,
                        (int(width * 0.5), int(height * 0.5)), interpolation = cv2.INTER_CUBIC)

# 将图片转为灰度图
img_gray = cv2.cvtColor(img_resize, cv2.COLOR_RGB2GRAY)
cv2.imshow("img_gray", img_gray)
print("img_gray shape:{}".format(np.shape(img_gray)))
cv2.waitKey()
