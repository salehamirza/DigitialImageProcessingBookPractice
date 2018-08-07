import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('cup.jpg',0)
hist,bins = np.histogram(img.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * hist.max()/ cdf.max()
cdf_m = np.ma.masked_equal(cdf,0)
cdf_m = (cdf_m - cdf_m.min())*255/(cdf_m.max()-cdf_m.min())
cdf = np.ma.filled(cdf_m,0).astype('uint8')
plt.plot(cdf_normalized, color = 'b')
img2 = cdf[img]
img = cv2.imread('wiki.jpg',0)
#OpenCV has a function to do this, cv2.equalizeHist(). 
# Its input is just grayscale image and output is our histogram equalized image
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ)) #stacking images side-by-side
cv2.imwrite('res.png',res)
cv2.imshow('HistogramEqualizationImage',res)
cv2.waitKey(0)
cv2.destroyAllWindows()