# Halftoning and QMC 半色调技术的拟蒙特卡罗算法实现

halftone is the Reproprinting technique that simulates *coninuous tone imagery* [one where each color at any point in the image is reproduced as a single tone, and not as distance halftonesD]    
through the use of dots, varying either in size or in spacing, thus generating a gradient-like effect.

半色调常见于印刷品,其中由浅到深的变化是靠网点面积大小或网店覆盖率来表现的,不同于Continuous-Tone Image是以单位面积成像物质颗粒密目来构成的;
![](src/2.png)
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
2. Split the image into C, M, Y, K.
3. Rotate each separated image by 0, 15, 30, and 45 degrees respectively.
4. Take the half-tone of each image (dot size will be proportional to the intensity).
5. Rotate back each half-toned image.
6. 代码详见 halftone.py ; 未整合 QMC algorithm



