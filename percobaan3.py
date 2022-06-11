# import library python package
import cv2
import numpy as np

# membaca file gambar len.jpg yang berada dalam folder  yang sama dengan file
image = cv2.imread("Taufik.jpg")

# menampilkan citra grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
