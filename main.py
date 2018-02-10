from numpy import *
import scipy.io
import pywt
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw


#image = scipy.misc.imread('girl.jpg',  mode='RGB')
image = scipy.misc.imread('temp.jpg', flatten='true',  mode='RGB')

#image = plt.imread('girl.jpg')

noiseVariance = 10
image += random.normal(0, noiseVariance, size=image.shape)
wavelet = pywt.Wavelet('db1')
#levels = int(floor(log2(image.shape[0])))
threhold = noiseVariance * sqrt(2*log2(image.size))

WaveletCoeffs = pywt.wavedec2(image, wavelet, level=2)
print(len(WaveletCoeffs))

# plt.plot(WaveletCoeffs[1][0])
# plt.show()

cA = pywt.threshold(WaveletCoeffs[0], 10, mode='soft')
cH = pywt.threshold(WaveletCoeffs[1][0], 200, mode='hard')
cV = pywt.threshold(WaveletCoeffs[1][1], 200, mode='hard')
cD = pywt.threshold(WaveletCoeffs[1][2], 200, mode='hard')

print(cH)
thresholded_wavelet =[cA, [cH, cV, cD]]

denoise_image = pywt.waverec2(thresholded_wavelet, wavelet)

print('Image', image)
print('Denoise image:', denoise_image)
plt.axis("off")
plt.figure(1)
plt.imshow(image)
plt.gray()
#plt.show()
plt.figure(2)
plt.imshow(denoise_image)
plt.show()