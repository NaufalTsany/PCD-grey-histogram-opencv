#memanggil library yang dipakai
import cv2
from matplotlib import pyplot as plt

#memanggil photo dari folder image
img = cv2.imread("image/orange.jpg")

#menampilkan gambar di jendela baru
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#menampilkan format dimensi gambar
print(img.shape)

#convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#menampilkan gambar di jendela baru
cv2.imshow("Gray",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#menampilkan format dimensi gambar
print(gray.shape)

#convert to grayscale dengan opencv
(thresh, binary) = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

#menampilkan gambar di jendela baru
cv2.imshow("Gray",binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

#menampilkan format dimensi gambar
print(binary.shape)

#menyimpan gambar sebagai file
cv2.imwrite("image/hasil-binary.png",binary)