import numpy as np
import cv2
from blur import blur
#这个python脚本用于测试blur的功能


#这里首先读取实例图片，先对整张图片做blur，qa可直接运行查看，这里会出现两张图片，查看完后任意键进入下一段测试
image = cv2.imread("test.jpg")

new_image = blur_version2(image, [(0,0,image.shape[0],image.shape[1])], 10)
cv2.imshow("image", image)
cv2.imshow("new", new_image)
cv2.waitKey()




#这里是第二段测试，也会出现两张那个图片，这里对其中一特定矩形区域blur，运行会显示被blur的区域，任意键进入下端测试
image = cv2.imread("test.jpg")
districts = [(800,1400,400,400)]
new_image = blur(image, districts, 10)

i = 0
for district in districts:
	cv2.imshow("image" + str(i), image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], :])
	cv2.imshow("new" + str(i), new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], :])
	i += 1

cv2.waitKey()


#这是第三段测试，选定另一个区域做blur
image = cv2.imread("test.jpg")
districts = [(100, 1400, 300, 300)]
new_image = blur(image, districts, 10)

i = 0
for district in districts:
	cv2.imshow("image" + str(i), image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], :])
	cv2.imshow("new" + str(i), new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], :])
	i += 1

cv2.waitKey()


#最后一段程序同时对两个区域blur，最后结果得到四张图片，两张区域原像，两张blur后的图像
image = cv2.imread("test.jpg")
districts = [(800,1400,400,400), [100, 1400, 300, 300]]
new_image = blur(image, districts, 10)

i = 0
for district in districts:
	cv2.imshow("image" + str(i), image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], :])
	cv2.imshow("new" + str(i), new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], :])
	i += 1

cv2.waitKey()





