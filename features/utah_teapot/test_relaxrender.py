import unittest

import features.utah_teapot.points as rp
import features.utah_teapot.color as color
import features.utah_teapot.mesh as mesh
import features.utah_teapot.example_scene as example
import features.utah_teapot.raycasting as raycasting
import features.utah_teapot.context as ctx
import features.utah_teapot.screenwriter as sw

class TestRelaxRender(unittest.TestCase):

    def test_simple_render(self):
        
        scene = example.cornell_box

        render = raycasting.SimpleReverseRayCasting(ctx.Context())
        input_xy, output_color = render.drive_raycasting(scene)
        
        writer = sw.NormalizedWriter(ctx.Context())
        writer.write(input_xy, output_color, 'output_test.jpg')

        
