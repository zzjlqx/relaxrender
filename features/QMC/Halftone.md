# Halftoning and QMC 半色调技术的拟蒙特卡罗算法实现

halftone is the Reproprinting technique that simulates *coninuous tone imagery* [one where each color at any point in the image is reproduced as a single tone, and not as distance halftonesD]    
through the use of dots, varying either in size or in spacing, thus generating a gradient-like effect.

半色调常见于印刷品,其中由浅到深的变化是靠网点面积大小或网店覆盖率来表现的,不同于Continuous-Tone Image是以单位面积成像物质颗粒密目来构成的;
![image2](src/2.png)
## Purpose
- render a gray-scale image by placing black dots on white background
- make halftone rendering look like origin gray-scale image
## Constraints
- resolution - size and spacing of dots, number of dots
- speed of rendering
## Various algorithmic approaches - MC integration techniques
we don't focus on other algotihm
1. 用n个点估计评价值积分$\int_R{f(x)dx}$;;


# overall 
[refer](https://stackoverflow.com/questions/10572274/halftone-images-in-python/10575940#10575940)

1. 用到python image library(PIL)
1. Split the image into C, M, Y, K.
1. [gcr](#gcr)
1. Rotate each separated image by 0, 15, 30, and 45 degrees respectively.
1. Take the half-tone of each image (dot size will be proportional to the intensity).
1. Rotate back each half-toned image.
1. 代码详见 halftone.py ; 未整合 QMC algorithm

## GCR
Within the CMY color space,
a range of colors can be achieved by combining the three primaries.
This combination in its turn can be thought of as a hue component
(which will require a maximum of two primary colors)
and a grey component
(a mixture of all three, in an appropriate quantity to give the required saturation).
If the grey component is replaced by black ink, the same color is being achieved by using two primaries and black. 
The act of substituting a quantity of black for the grey component is known as "Grey component replacement" (GCR).

