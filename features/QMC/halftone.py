import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageStat as ImageStat
import os

"""
The bulk of this is taken from this Stack Overflow answer by fraxel:
http://stackoverflow.com/a/10575940/250962
"""


class Halftone:
    def __init__(self, path):
        """
        :param path: eg: ./src/1.jpeg
        """
        self.path = path

    def make(self, sample=10, scale=1, angles=[0, 15, 30, 45], antialias=False, style='color', percentage=0,filename_add='_halftoned'):
        """
            sample: Sample box size from original image, in pixels.
            scale: Max output dot diameter is sample*scale
            angles: A list of 4 angles that each screen channel should be rotated by
            style: 'color' or 'grayscale'
            antialias: true or false
            percentage: How much of the gray component to remove from the CMY channels
                and put in the K channel
            filename_add: output filename
        """

        # try:
        im = Image.open(self.path)
        # except IOError:
            # print("Cannot open such image...")
            # raise

        if style == 'grayscale':
            angles = angles[:1]
            gray_im = im.convert('L')  # mode:8位像素
            dots = self.halftone(gray_im, sample, scale, angles, antialias)
            new = dots[0]

        else:
            cmyk_im = im.convert('CMYK')
            cmyk_im_merge = self.gcr(cmyk_im, percentage)
            dots = self.halftone(cmyk_im_merge, sample, scale, angles, antialias)
            new = Image.merge('CMYK', dots)  # mode:4*8 位像素,颜色分离

        f, e = os.path.splitext(self.path)
        outfile = "%s%s%s" % (f, filename_add, e)
        new.save(outfile)

    def gcr(self, im, percentage):
        """
        gcr: Gray Component Replacement
            Returns a CMYK image with percentae gray component removed from the CMY channels
            and put in the K channel,
                ie for percentage = 80, (30, 100, 255, 0) >> (6, 76, 231, 24)
        """
        if not percentage:
            return im
        cmyk_arr = im.split()
        cmyk = []
        for i in range(4):
            cmyk.append(cmyk_arr[i].load())
        for x in range(im.size[0]):  # for x axis pixels
            for y in range(im.size[1]):  # for y axis pixels
                gray = min(cmyk[0][x, y], cmyk[1][x, y], cmyk[2][x, y]) * percentage / 100
                for i in range(3):
                    cmyk[i][x, y] -= int(gray)
                cmyk[3][x, y] = int(gray)
        return Image.merge('CMYK', cmyk_arr)

    def halftone(self, cmyk, sample, scale, angles, antialias):
        """
        Returns list of half-tone images for cmyk image.
        So sample=1 will presevere the original image resolution,
        (but scale must be >1 to allow variation in dot size.)
        """
        if antialias is True:
            antialias_scale = 4
            # multiple the size of the image by this scale
            # while drawing and scaling back down when merge
            scale *= antialias_scale

        dots = []

        for channel, angle in zip(cmyk.split(), angles):
            channel = channel.rotate(angle, expand=1)
            size = channel.size[0] * scale, channel.size[1] * scale
            half_tone = Image.new('L', size)
            draw = ImageDraw.Draw(half_tone)
            # Cycle through one sample point at a time, drawing a circle for each one:
            for x in range(0, channel.size[0], sample):
                for y in range(0, channel.size[1], sample):
                    # Area we sample to get the level:
                    box = channel.crop((x, y, x + sample, y + sample))

                    # The average level for that box (0-255):
                    mean = ImageStat.Stat(box).mean[0]

                    # The diameter of the circle to draw based on the mean (0-1):
                    diameter = (mean / 255) ** 0.5

                    # Size of the box we'll draw the circle in:
                    box_size = sample * scale

                    # Diameter of circle we'll draw:
                    # If sample=10 and scale=1 then this is (0-10)
                    draw_diameter = diameter * box_size

                    # Position of top-left of box we'll draw the circle in:
                    # x_pos, y_pos = (x * scale), (y * scale)
                    box_x, box_y = (x * scale), (y * scale)

                    # Positioned of top-left and bottom-right of circle:
                    # A maximum-sized circle will have its edges at the edges
                    # of the draw box.
                    x1 = box_x + ((box_size - draw_diameter) / 2)
                    y1 = box_y + ((box_size - draw_diameter) / 2)
                    x2 = x1 + draw_diameter
                    y2 = y1 + draw_diameter

                    draw.ellipse([(x1, y1), (x2, y2)], fill=255)

            half_tone = half_tone.rotate(-angle, expand=1)
            width_half, height_half = half_tone.size

            # Top-left and bottom-right of the image to crop to:
            xx1 = (width_half - cmyk.size[0] * scale) / 2
            yy1 = (height_half - cmyk.size[1] * scale) / 2
            xx2 = xx1 + cmyk.size[0] * scale
            yy2 = yy1 + cmyk.size[1] * scale

            half_tone = half_tone.crop((xx1, yy1, xx2, yy2))

            if antialias is True:
                w = (xx2 - xx1) / antialias_scale
                h = (yy2 - yy1) / antialias_scale
                half_tone = half_tone.resize((int(w), int(h)), resample=Image.LANCZOS)
            dots.append(half_tone)
        return dots
