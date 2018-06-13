import unittest
import numpy as np
from .render import Render



class Test(unittest.TestCase):

    def test_array(self):    #根据接口命名测试的函数名 如 test_size 
        Render.render_array_to_array()           #函数内调用我们的类 
