import unittest

from features.spatial_denoising.clear_noise import ClearNoise


class TestSpatialDenoising(unittest.TestCase):

    def test_spatail_denoising_mid(self):

        clear = ClearNoise()

        images = clear.clear_noise_mid()
        diff=self.diff_of_images(images)
        self.assertTrue(diff <= 0.1)

    def test_spatail_denoising_ave(self):

        clear = ClearNoise()

        images = clear.clear_noise_ave()
        diff=self.diff_of_images(images)
        self.assertTrue(diff <= 0.1)

    # 判断去噪结果和原图的偏差
    def diff_of_images(self,images):
        pix1 = images[0]
        pix2 = images[1]

        w, h = images[2]
        tot = 0

        for i in range(0, w):
            for j in range(0, h):
                tmp = abs(pix1[j, i] - pix2[j, i])
                tot += tmp / 255

        return tot / (w * h)

if __name__ == '__main__':
    unittest.main()
