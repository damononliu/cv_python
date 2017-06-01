from PIL import Image
from numpy import *
from pylab import *
from scipy.ndimage import filters


im = array(Image.open('../data/empire.jpg').convert('L'))

figure()
gray()

subplot(121)
axis('off')
imshow(im)

sigma = 3

imx = zeros(im.shape)
#imx = filters.gaussian_filter(im, sigma)
imx = im + 0.4 * (im - filters.gaussian_filter(im, sigma))
imx = clip(imx, 0, 255)

subplot(122)
axis('off')
#axis('equal')
imshow(imx)

#figure()
#gray()
#imshow(imx)

show()
