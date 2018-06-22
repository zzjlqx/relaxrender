import unittest
import numpy as np
from .render import *
from skimage import data



class Test(unittest.TestCase):

    def test_array(self):    #根据接口命名测试的函数名 如 test_size 
        img = data.coffee()
        render_array_to_array(img,1/2.2)           #函数内调用我们的类 
        
        
