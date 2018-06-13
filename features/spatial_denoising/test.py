import unittest

from features.spatial_denoising.clear_noise import ClearNoise




class TestSpatialDenoising(unittest.TestCase):

    def __init__(self):
        self.clear=ClearNoise()

    def test_spatail_denoising(self):

        images=self.clear.clear_noise()

        t = self.test_images(images)


        self.assertTrue(t<=0.1)

    def test_images(self,images):
        pix1 = images[0].load()
        pix2 = images[1].load()

        w, h = images[0].size
        w -= 1
        h -= 1

        tot = 0

        for i in range(0, w):
            for j in range(0, h):
                tmp = abs(pix1[j, i] - pix2[j, i])
                tot += tmp / 255

        return tot / (w * h)

