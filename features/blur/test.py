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




"""
image = cv2.imread("test.jpg")
districts = [(800,1400,400,400)]
new_image = blur(image, districts, 10)

i = 0
for district in districts:
	cv2.imshow("image" + str(i), image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], :])
	cv2.imshow("new" + str(i), new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], :])
	i += 1

cv2.waitKey()



image = cv2.imread("test.jpg")
districts = [(100, 1400, 300, 300)]
new_image = blur(image, districts, 10)

i = 0
for district in districts:
	cv2.imshow("image" + str(i), image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], :])
	cv2.imshow("new" + str(i), new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], :])
	i += 1

cv2.waitKey()


image = cv2.imread("test.jpg")
districts = [(800,1400,400,400), [100, 1400, 300, 300]]
new_image = blur(image, districts, 10)

i = 0
for district in districts:
	cv2.imshow("image" + str(i), image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], :])
	cv2.imshow("new" + str(i), new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], :])
	i += 1

cv2.waitKey()
"""
