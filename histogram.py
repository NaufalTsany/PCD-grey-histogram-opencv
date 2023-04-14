#memanggil library yang digunakan
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from skimage import data
from skimage.io import imread
from skimage.filters import threshold_minimum
from skimage.filters import threshold_mean

#memanggil photo dari file
grayImage = imread(fname="image/dog.jfif")
print('gray image shape : ',grayImage.shape)

#memanggil photo dari file
rgbImage = imread(fname="image/slf.jpeg")
print('rgb image shape : ',rgbImage.shape)

#menentukan ukuran plot menggunakan library matplotlib
fig, axes = plt.subplots(2, 1, figsize=(12, 12))
ax = axes.ravel()

#membuat judul dan subplot yang ingin ditampilkan
ax[0].imshow(grayImage, cmap=plt.cm.gray)
ax[0].set_title("Grayscale Image")
ax[1].hist(grayImage.ravel(), bins=256)
ax[1].set_title('Histogram')

#memisahkan R, G, dan B pada gambar
red = rgbImage[:,:,0]
green = rgbImage[:,:,1]
blue = rgbImage[:,:,2]

#menampilkan dimensi pada masing masing RGB
print('Red Shape = ',red.shape)
print('Green Shape = ',green.shape)
print('Blue Shape = ',blue.shape)

#menentukan ukuran plot menggunakan library matplotlib
fig, axes = plt.subplots(3, 3, figsize=(12, 12))
ax = axes.ravel()

#membuat judul dan subplot yang ingin ditampilkan
ax[3].imshow(rgbImage)
ax[3].set_title("Original")

ax[1].imshow(red, cmap=plt.cm.gray)
ax[1].set_title("Red Channel")
ax[2].hist(red.ravel(), bins=256)
ax[2].set_title('Histogram')

ax[4].imshow(green, cmap=plt.cm.gray)
ax[4].set_title("Green Channel")
ax[5].hist(green.ravel(), bins=256)
ax[5].set_title('Histogram')

ax[7].imshow(blue, cmap=plt.cm.gray)
ax[7].set_title("Blue Channel")
ax[8].hist(blue.ravel(), bins=256)
ax[8].set_title('Histogram')

#menampilkan plot
fig.tight_layout()
plt.show()