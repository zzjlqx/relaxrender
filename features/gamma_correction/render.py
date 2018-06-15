# from skimage import data, io
# import matplotlib.pyplot as plt


# img = data.coffee()
# x = img/255
# gamma = 1/2.2
# img_new = x**gamma
# plt.figure()
# ax1=plt.subplot(121)
# ax2=plt.subplot(122)
# ax1.imshow(x)
# ax2.imshow(img_new)
# plt.show()

def render_array_to_array( img_array, gamma_value):
    x = img_array/255
    img_new = x**gamma_value
    return img_new
