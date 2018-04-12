import image_extract_array
import wavelet_thresholding
import main


def denoising_image(image, wavelet, level_of_transformation, threshold, mode_thresholding):
    '''
    :param image: path to image;
    :param wavelet: 'haar', 'db', 'sym', 'coif', 'bior', 'rbio', 'dmey', 'gaus'
    :param level_of_transformation:
    :param threshold: thresholding value;
    :param mode_thresholding: {'soft', 'hard', 'greater', 'less'}
    :return: denoised image array;
    '''

    image_array = image_extract_array.get_image_array(image)
    Y = image_extract_array.transform_coefficients_from_rgb_to_yuv(image_array, 0.299, 0.578, 0.114)
    U = image_extract_array.transform_coefficients_from_rgb_to_yuv(image_array, 0.1678, -0.3313, 0.5)
    V = image_extract_array.transform_coefficients_from_rgb_to_yuv(image_array, 0.5, -0.4187, 0.0813)

    WaveletCoefficients = wavelet_thresholding.wavelet_decomposition(Y, wavelet, level_of_transformation)
    thresholded_wavelet = wavelet_thresholding.wavelet_thresholding(WaveletCoefficients, threshold, mode_thresholding)
    denoised_array = wavelet_thresholding.wavelet_reconstruction(thresholded_wavelet, wavelet)
    denoised_rgb_image_array = image_extract_array.transform_coefficients_from_yuv_to_rgb(denoised_array, U, V)

    return denoised_rgb_image_array



main.show_image(denoising_image('boy.jpg', 'db1', 5, [1, 1, 1, 1], 'soft'))
#print(denoising_image('a713.jpg', 'db1', 2, [5, 5, 5, 5], 'soft'))
#main.image_show_PIL(denoising_image('temp.jpg', 'db1', 2, [5, 5, 5, 5], 'soft'))

