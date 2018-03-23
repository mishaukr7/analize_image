import scipy.io


def get_image_array(image):
    '''

    :param image: path to image;
    :return: list of RGB color.
    '''
    return scipy.misc.imread(image, mode='RGB')


def transform_coefficients_from_rgb_to_yuv(input_array, a, b, c):
    '''
    Transform RGB format to YUV (grayscale layer format)
    :param input_array: array of input data
    :param a: coefficient a
    :param b: coefficient b
    :param c: coefficient c
    :return: array YUV-format of image.
    '''
    transform_list = []
    for first_list in input_array:
        first_list_transform = []
        for second_list in first_list:
            first_list_transform.append(second_list[0] * a + second_list[1] * b + second_list[2] * c)
        transform_list.append(first_list_transform)
    return transform_list


def transform_coefficients_from_yuv_to_rgb(Y, U, V):
    '''
    Transform RGB format to YUV (grayscale layer format).
    :param Y: array of Y-сomponent grayscale layer of image;
    :param U: array of U-сomponent grayscale layer of image
    :param V: array of V-сomponent grayscale layer of image
    :return: array RGB-format of image.
    '''
    transform_list = []
    for y_list, u_list, v_list in Y, U, V:
        transform_list_internal = []
        for y_list_internal, u_list_internal, v_list_internal in y_list, u_list, v_list:
            R = y_list_internal + 1.3707 * (v_list_internal - 128)
            G = y_list_internal - 0.3365 * (u_list_internal - 128) - 0.6982*(v_list_internal - 128)
            B = y_list_internal + 1.7324 * (u_list_internal - 128)
            transform_list_internal_three_value = [R, G, B]
            transform_list_internal.append(transform_list_internal_three_value)
        transform_list.append(transform_list_internal)
    return transform_list









#print(transform_coeff(get_image_array('temp.jpg'), 0.299, 0.587, 0.114)[2])


#def transformation_image_to_YUV(image):

#print(get_image_array('temp.jpg'))

transform_coefficients_from_rgb_to_yuv(get_image_array('temp.jpg'), 0.299, 0.587, 0.114)