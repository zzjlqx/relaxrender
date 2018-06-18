gauss_kernel = numpy.array([[1,2,1],
				[2,4,1],
				[1,2,1]]) * 1.0/16

def blur_naive_version(iamge, districts, scale):
	if(len(image.shape)!=3):
		print("error")
		exit(0)
		
	new_image = image.copy()
	
	for district in districts:
		new_image = gauss_blur_naive_version(new_image, district, scale)
		
	return new_image


def 
