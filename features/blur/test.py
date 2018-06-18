import numpy as np
import cv2
from blur import *


image = cv2.imread("test.jpg")

new_image = blur(image, [(0,0,image.shape[0],image.shape[1])], 20)
cv2.imshow("image", image)
cv2.imshow("new", new_image)
cv2.waitKey()

new_image = blur_version2(image, [(0,0,image.shape[0],image.shape[1])], 10)
cv2.imshow("image", image)
cv2.imshow("new", new_image)
cv2.waitKey()



