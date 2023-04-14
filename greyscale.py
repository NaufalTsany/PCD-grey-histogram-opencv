#import library yang digunakan
import matplotlib.pyplot as plt
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray

#memanggil, membaca, dan melihat bentuk/format gambar yang diambil dari skimage dan local file
astroImage = data.astronaut()
loadImage = imread(fname="image/slf.jpeg")
print('astroImage shape = ',astroImage.shape)
print('loadImage shape = ',loadImage.shape)

#merubah format gambar menjadi greyscale
astroGray = rgb2gray(astroImage)
loadGray = rgb2gray(loadImage)
print('astroGray shape = ',astroGray.shape)
print('loadGray shape = ',loadGray.shape)

#menentukan ukuran plot menggunakan library matplotlib
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
ax = axes.ravel()

#membuat judul dan subplot yang ingin ditampilkan
ax[0].imshow(astroImage)
ax[0].set_title("Astronaut RGB Image")
ax[1].imshow(loadImage)
ax[1].set_title("Load RGB Image")
ax[2].imshow(astroGray,cmap=plt.cm.gray)
ax[2].set_title("Astronaut Grayscale Image")
ax[3].imshow(loadGray,cmap=plt.cm.gray)
ax[3].set_title("Load Grayscale Image")

#merubah gambar grayscale secara manual
astroGray = astroImage.copy()
astroGray = (astroGray[:,:,0]*0.299) + (astroGray[:,:,0]*0.7154) + (astroGray[:,:,0]*0.0721)
loadGray = loadImage.copy()
loadGray = (loadGray[:,:,0]*0.299) + (loadGray[:,:,0]*0.7154) + (loadGray[:,:,0]*0.0721)
print('astroGray shape = ',astroGray.shape)
print('loadGray shape = ',loadGray.shape)

#menentukan ukuran plot menggunakan library matplotlib
fig, axes = plt.subplots(1, 2, figsize=(10, 10))
ax = axes.ravel()

#membuat judul dan subplot yang ingin ditampilkan
ax[0].imshow(astroGray, cmap=plt.cm.gray)
ax[0].set_title("Original")
ax[1].imshow(loadGray, cmap=plt.cm.gray)
ax[1].set_title("Grayscale")

#memunculkan plot
fig.tight_layout()
plt.show()