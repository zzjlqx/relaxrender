import numpy
import cv2
from scipy import ndimage

def blur(image, districts, scale):
	if(len(image.shape)!=3):
		print("error")
		exit(0)
	new_image = image.copy()
	for district in districts:
		new_image = gauss_blur(new_image, district, scale)
	return new_image


def gauss_blur(image, district, scale):
	if(image.shape[0] < district[0] + district[2] or image.shape[1] < district[1] + district[3]):
		print("error district")
		exit(1)
	
	gaussian = numpy.array([[1,2,1],[2,4,2],[1,2,1]]) * 1.0/16
	
	new_image = image.copy()
	for r in range(scale):
		for i in range(3):
			new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], i] = ndimage.convolve(new_image[district[0]:district[0]+district[2], district[1]:district[1]+district[3], i], gaussian)
	return new_image
	

