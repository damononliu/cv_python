# -*- coding: utf-8 -*-

from PIL import Image

from pylab import *

from numpy import *

from scipy.ndimage import filters

import copy

#读取图片,灰度化并转为数组
im = array(Image.open('../data/empire.jpg'))

#r通道
r = im[:,:,0]

#g通道
g = im[:,:,1]

#b通道
b = im[:,:,2]


#对r通道进行σ = 2的高斯滤波
r = filters.gaussian_filter(r,2)

#对g通道进行σ = 2的高斯滤波
g = filters.gaussian_filter(g,2)

#对b通道进行σ = 2的高斯滤波
b = filters.gaussian_filter(b,2)

#组合各通道
im2 = copy.deepcopy(im)

im2[:,:,0] = r

im2[:,:,1] = g

im2[:,:,2] = b

#显示图像
subplot(121)
axis('off')
title('source')

imshow(im)

subplot(122)
axis('off')
title('After GaussFilter')

imshow(im2)

show()         