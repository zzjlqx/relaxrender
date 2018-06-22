import unittest
from .render import *
from skimage import data



class Test(unittest.TestCase):

    def test_gamma(self):    
        img = data.coffee()                  #测试图片用例
        gamma_correction(img,2.2,1,1,1)           #函数内调用我们的类 
        gamma_correction(img,2.2,2)
        gamma_correction(img,2.2,3)
     
        
        
