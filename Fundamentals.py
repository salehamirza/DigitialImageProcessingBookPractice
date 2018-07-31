#Importing the Libraries for Image Processing 
import numpy as np
import cv2
#Reading Image
img = cv2.imread('cup.jpg')
#Displaying Image
cv2.imshow('image',img)
#Writing image
cv2.imwrite('imgWrite.png',img)
#Changing color of a pixel to Red 
img = cv2.imread('w.png')
redcolor = (255,0,0)
img[100,150]=redcolor
cv2.imshow('PixelColorChanged',img)
cv2.waitKey(0)
cv2.destroyAllWindows()