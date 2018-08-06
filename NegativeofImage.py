import sys
import cv2

print("Python version: \n" + sys.version)
print("cv2 version: " + cv2.__version__)

#img1 and img2 must be in same size
img1 = cv2.imread('cup.jpg', 1)
img2 = (255-img1)

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

cv2.waitKey(0)
cv2.destroyAllWindow()
