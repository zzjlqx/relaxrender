# coding:utf-8
from PIL import Image, ImageDraw


class ClearNoise:

    # 判断噪点
    # 将灰度值与周围灰度值相似度较小的点认为是噪点
    def clearNoise(self, img, radius, m, func):
        pix = img.load()
        w, h = img.size
        w -= 1
        h -= 1

        for i in range(0, w):
            for j in range(0, h):
                sim = -1
                # 认为这个点是噪点
                for k in range(i - radius, i + radius):
                    if k < 1 or k > w:
                        continue
                    for q in range(j - radius, j + radius):
                        if q <= 1 or q > h:
                            continue
                        if abs(pix[k, q] - pix[i, j]) < 40:
                            sim += 1
                # 该点与周围点相似度较小，认为是噪点
                if sim < m:
                    tmp = func(pix, i, j, radius, w, h)
                    pix[i, j] = tmp

    # 平均值去噪
    # 用噪点领域的内的平均值代替噪点
    def ave_of_rec(self, pix, x, y, radius, w, h):
        p = 0
        num = 0

        for i in range(x - radius, x + radius):
            if i < 1 or i > w:
                continue
            for j in range(y - radius, y + radius):
                if j <= 1 or j > h:
                    continue
                # 排除极值点
                if pix[i, j] > 15 and pix[i, j] < 230:
                    p += pix[i, j]
                    num += 1
        return p // num

    # 中值去噪
    # 用噪点领域的中值代替噪点
    def mid_of_rec(self, pix, x, y, radius, w, h):
        p = []

        for i in range(x - radius, x + radius):
            if i < 1 or i > w:
                continue
            for j in range(y - radius, y + radius):
                if j <= 1 or j > h:
                    continue
                # 排除极值点
                if pix[i, j] > 15 and pix[i, j] < 230:
                    p.append(pix[i, j])

        p.sort()
        m = len(p) // 2
        '''
        if m <= 0:
            px = x + radius
            py = y + radius
            if px > w:
                px = w
            if py > h:
                py = h

            return pix[px, py]
        else:
        '''
        return (p[m] + p[-m]) // 2

    def clear_noise_mid(self):

        # 打开图片
        image = Image.open("./test.jpeg").convert('L')
        img = Image.open("./原图.bmp").convert('L')

        # 采用中值去噪
        self.clearNoise(image, 3, 9, self.mid_of_rec)

        # 保存图片
        image.save("./中值去噪.jpeg")
        pix_1 = image.load()
        pix_2 = img.load()

        image.close()
        img.close()

        return (pix_1, pix_2, image.size)

    def clear_noise_ave(self):

        # 打开图片
        image = Image.open("./test.jpeg").convert('L')
        img = Image.open("./原图.bmp").convert('L')

        # 采用均值去噪
        self.clearNoise(image, 3, 9, self.ave_of_rec)

        # 保存图片
        image.save("./均值去噪.jpeg")
        pix_1 = image.load()
        pix_2 = img.load()

        image.close()
        img.close()

        return (pix_1, pix_2, image.size)
