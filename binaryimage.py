#memanggil library yang dipakai
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from skimage import data
from skimage.filters import threshold_otsu
from skimage.filters import threshold_minimum
from skimage.filters import threshold_mean

#memanggil photo camera dari library skimage
image = data.camera()

#memberikan Threshold Minimum dan convert image to binary image
threshMin = threshold_minimum(image)
print('Threshold Minimum : ',threshMin)
minimumImage = image > threshMin

#memberikan Threshold Minimum dan convert image to binary image
threshMean = threshold_mean(image)
print('Threshold Mean : ',threshMean)
meanImage = image > threshMean

#menentukan ukuran plot menggunakan library matplotlib
fig, axes = plt.subplots(3, 2, figsize=(12, 12))
ax = axes.ravel()

#membuat judul dan subplot yang ingin ditampilkan (1,2)
ax[0].imshow(image, cmap=plt.cm.gray)
ax[0].set_title("Original")
ax[1].hist(image.ravel(), bins=256)
ax[1].set_title('Histogram')

#membuat judul dan subplot yang ingin ditampilkan (2,2)
ax[2].imshow(minimumImage, cmap=plt.cm.gray)
ax[2].set_title('Thresholded (min)')
ax[3].hist(image.ravel(), bins=256)
ax[3].axvline(threshMin, color='r')
ax[3].set_title('Histogram (min)')

#membuat judul dan subplot yang ingin ditampilkan (3,2)
ax[4].imshow(meanImage, cmap=plt.cm.gray)
ax[4].set_title('Thresholded (mean)')
ax[5].hist(image.ravel(), bins=256)
ax[5].axvline(threshMean, color='r')
ax[5].set_title('Histogram (mean)')

#memunculkan plot
plt.tight_layout()
plt.show()