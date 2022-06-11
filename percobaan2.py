from contextlib import closing
import cv2 as cv2
import numpy as np

# kode program erosi
img = cv2.imread("Taufik.jpg")
kernel = np.ones((5, 5), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)
cv2.imshow("Erotion", dilation)

cv2.waitKey(0)
cv2.destroyAllWindows()