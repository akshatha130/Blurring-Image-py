import cv2
import numpy as np

img = cv2.imread("Lenna.png") 
img = cv2.resize(img,(400,400))
cv2.imshow("original_img",img)

kernel = np.ones((5,5),np.float32)/25

homo = cv2.filter2D(img,-1,kernel)
cv2.imshow("homogeneous",homo)

gau = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("gaussian",gau)

cv2.imshow("image",kernel)

cv2.waitKey(0)
cv2.destroyAllWindows()
