import numpy as np
import imageio
import scipy.ndimage
import cv2

img = "IMG_8577.jpg "

def rgb2gray(rgb):
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])    #2D array formula to convert image to grayscale

def dodge(front, back):
    final_sketch = front*255/(255-back)
    final_sketch[final_sketch>255]=255
    final_sketch[back == 255]=255
    return final_sketch.astype('uint8')

ss = imageio.imread(img)  #to read the given image
gray = rgb2gray(ss)          #to change image to black and white first


i = 255-gray   #0,0,0 is for darkest color and 255,255,255 is for brighest color which is probably white

#to convert to blur

blur = scipy.ndimage.filters.gaussian_filter(i, sigma = 15) #sigma is intensity of blurness of image
r = dodge(blur, gray)

cv2.imwrite('bsketch.png', r)

