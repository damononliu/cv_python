 # -*- coding: utf-8 -*-

from PIL import Image

#对Pyplot的解说：“方便快速绘图matplotlib通过pyplot模块提供了一套和MATLAB类似的绘图API，
#将众多绘图对象所构成的复杂结构隐藏在这套API内部。”

#对pylab的解说：“matplotlib还提供了一个名为pylab的模块，其中包括了许多NumPy和pyplot
#模块中常用的函数，方便用户快速进行计算和绘图，十分适合在IPython交互式环境中使用。”

from pylab import *

# 添加中文字体支持
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc", size=14)
im = array(Image.open('../data/empire.jpg').convert('L'))  # 打开图像，并转成灰度图像

figure()
subplot(121)
gray()
contour(im, origin='image')
axis('equal')
axis('off')
title(u'图像轮廓', fontproperties=font)

subplot(122)
hist(im.flatten(), 128)
title(u'图像直方图', fontproperties=font)

plt.xlim([0,260]) # 这里可以直接引用plt，就是因为在pylab的源代码中已经import matplotlib.pyplot as plt
plt.ylim([0,11000])

show()
