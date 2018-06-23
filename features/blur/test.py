import numpy as np
import cv2
import unittest
from blur import blur
#这个python脚本用于测试blur的功能

class TestBlur(unittest.TestCase):
	def setUp(self):
		#读取我们要模糊的图片
		self.image = cv2.imread('test.jpg')
		self.blur = blur
		self.scale = 20
		
		
	#test the selected area of input image
	#对于这个测试我们模糊科比身上24号码对应的区域
	def test_some_area_pic(self):
		new_image = self.blur(self.image, [(900,1200,500,700)], self.scale)
		cv2.imwrite("after_blur_some_area_pic.jpg", new_image)


	#test the whole area of input image
	#模糊整张图片
	def test_whole_pic(self):
		#选中区域对图像进行模糊
		new_image = self.blur(self.image, [(0,0,self.image.shape[0],self.image.shape[1])], self.scale)
		cv2.imwrite("after_blur_whole_pic.jpg", new_image)
		


if(__name__ == "__main__"):
	unittest.main()



