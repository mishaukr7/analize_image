import pywt


def wavelet_decomposition(input_array, wavelet_family, level_transformation):
    '''

    :param input_array: array of image file
    :param wavelet_family: 'haar', 'db', 'sym', 'coif', 'bior', 'rbio', 'dmey', 'gaus'
    :param level_transformation:
    :return: wavelet coefficients: Approximation, horizontal detail, vertical detail and diagonal detail coefficients respectively
    '''
    wavelet_transformation = pywt.Wavelet(wavelet_family)
    WaveletCoeffs = pywt.wavedec2(input_array, wavelet_transformation, level=level_transformation)
    return WaveletCoeffs


def wavelet_thresholding(array_of_wavelet_coeff, threshold, mode_thresholding):
    '''
    :param array_of_wavelet_coeff:  wavelet coefficients: Approximation, horizontal detail, vertical detail
            and diagonal detail coefficients respectively
    :param thresholdcA: threshold for Approximation component;
    :param thresholdcH: threshold for horizontal detail;
    :param thresholdcV: threshold for vertical detail;
    :param thresholdcD: threshold for diagonal detail;
    :param mode_thresholding: {'soft', 'hard', 'greater', 'less'}
    :return: thresholded wavelet coefficients.
    '''

    cA = pywt.threshold(array_of_wavelet_coeff[0], threshold[0], mode=mode_thresholding)
    cH = pywt.threshold(array_of_wavelet_coeff[1][0], threshold[1], mode=mode_thresholding)
    cV = pywt.threshold(array_of_wavelet_coeff[1][1], threshold[2], mode=mode_thresholding)
    cD = pywt.threshold(array_of_wavelet_coeff[1][2], threshold[3], mode=mode_thresholding)

    thresholded_wavelet = [cA, [cH, cV, cD]]

    return thresholded_wavelet


def wavelet_reconstruction(thresholded_wavelet_coefficents, wavelet_family):

    '''

    :param thresholded_wavelet_coefficents:
    :param wavelet_family:
    :return:
    '''
    wavelet_transformation = pywt.Wavelet(wavelet_family)

    denoise_image_array = pywt.waverec2(thresholded_wavelet_coefficents, wavelet_transformation)

    return denoise_image_array

