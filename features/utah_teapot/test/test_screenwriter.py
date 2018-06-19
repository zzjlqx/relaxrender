import unittest
import numpy as np

import features.utah_teapot.points as rp
import features.utah_teapot.color as color
import features.utah_teapot.screenwriter as sw
import features.utah_teapot.context as ctx

class TestPoints(unittest.TestCase):

    def test_normalizedwriter(self):
        sample_size = 100
        input_xy = np.random.random((int(sample_size), 2))*2-1
        output_color = np.random.random((int(sample_size), 3))
        output_color[input_xy[:, 0] > input_xy[:, 1], :] = 0

        writer = sw.NormalizedWriter(ctx.Context())
        writer.write(input_xy, output_color, 'output_points.jpg')
        
        #self.assertEqual(points.data[:points.cindex].shape, (2, 15))
