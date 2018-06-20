import unittest
from features.stochastic_ray_tracing.main import STRRelaxRender

class TestSTRRelaxRender(unittest.TestCase):

    def test_render(self):
        test = STRRelaxRender()
        test.render()