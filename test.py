from numpy import *
import scipy.io
import pywt
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import random


#image = scipy.misc.imread('girl.jpg',  mode='RGB')
#print(image)
#image = scipy.misc.imread('temp.jpg', flatten='true',  mode='RGB')

#image = plt.imread('girl.jpg')

#noiseVariance = 10
#image += random.normal(0, noiseVariance, size=image.shape)
#levels = int(floor(log2(image.shape[0])))
#threhold = noiseVariance * sqrt(2*log2(image.size))

#print(len(WaveletCoeffs))

# plt.plot(WaveletCoeffs[1][0])
# plt.show()

#cA = pywt.threshold(WaveletCoeffs[0], 10, mode='soft')
#cH = pywt.threshold(WaveletCoeffs[1][0], 200, mode='soft')
#cV = pywt.threshold(WaveletCoeffs[1][1], 200, mode='soft')
#cD = pywt.threshold(WaveletCoeffs[1][2], 200, mode='soft')

#print(cH)

#denoise_image = pywt.waverec2(thresholded_wavelet, wavelet)

#print('Image', image)
#print('Denoise image:', denoise_image)
# plt.axis("off")
# plt.figure(1)
# plt.imshow(image)
# plt.gray()
# #plt.show()
# plt.figure(2)
# plt.imshow(denoise_image)
# plt.show()

#print(thresholded_wavelet)
arr_input = []
for x in range(10):
    arr_input.append([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)])
print(arr_input)
wavelet = pywt.Wavelet('db1')
WaveletCoeffs = pywt.wavedec2(arr_input, wavelet, level=1)
thresholded_wavelet = pywt.threshold(WaveletCoeffs, 200, mode='soft')
denoise_arr = pywt.waverec2(thresholded_wavelet, wavelet)
print(denoise_arr)