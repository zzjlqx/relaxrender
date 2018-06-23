import numpy
from scipy import ndimage

'''采用高斯模糊的方法，通过高斯模糊矩阵对每个3*3的像素点进行卷积'''
def blur(image, districts, scale):
		
	new_image = image.copy()
	
	for district in districts:
		new_image = gauss_blur(new_image, district, scale)
		
	return new_image


def gauss_blur(image, district, scale):
	
    #高斯模糊矩阵求每个像素矩阵的加权平均
	gaussian = numpy.array([[1,2,1],
							[2,4,2],
							[1,2,1]]) * 1.0/16
	
	new_image = image.copy()
	for r in range(scale):
		for i in range(3):
			#对特定区域图像每个通道做高斯滤波
			new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], i] = ndimage.convolve(new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], i], gaussian)
	return new_image
