#memanggil library yang digunakan
import cv2
import numpy as np

#membaca photo yang digunakan
citra = cv2.imread('image/logo.png')

#menampilkan gambar dengan opencv di jendela baru
cv2.imshow("citra asli", citra)
cv2.waitKey()
cv2.destroyAllWindows()

#menampilkan tipe data dan dimensi
print(citra.shape)
print(citra.dtype)

#memisahkan nilai R, G , dan B pada gambar
b = citra[:,:,0]
g = citra[:,:,1]
r = citra[:,:,2]

panjang = len(citra)
lebar = len(citra[0])

#covert to grayscale  menggunakan numpy
citra_gray = np.zeros((panjang,lebar))

for i in range (panjang):
    for j in range (lebar):
        citra_gray[i,j] = 0.2989 * r[i,j] + 0.587 * g[i,j] + 0.1141 * b[i,j]

citra_gray = citra_gray.astype(np.uint8)

#menampilkan gambar dengan opencv di jendela baru
cv2.imshow("ABU", citra_gray)
cv2.waitKey()
cv2.destroyAllWindows()

#menampilkan matrix dari gambar
print(citra_gray)

#convert gambar from grayscale to binary image
panjang = len(citra)
lebar = len(citra[0])

ambang = 210

citra_biner = np.zeros((panjang,lebar))

for i in range (panjang):
    for j in range (lebar):
        if citra_gray[i,j] >= ambang:
          citra_biner[i,j] = 0
        else:
          citra_biner[i,j] = 1

#menampilkan gambar dengan opencv di jendela baru
cv2.imshow("biner", citra_biner)
cv2.waitKey()
cv2.destroyAllWindows()

#menampilkan pixel gambar grayscale
print(citra_gray[50,50])

#menampilkan pixel gambar biner
print(citra_biner[50,50])