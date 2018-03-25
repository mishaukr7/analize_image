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


def transform_coefficients_from_yuv_to_rgb1(Y, U, V):
    '''
    Transform RGB format to YUV (grayscale layer format).
    :param Y: array of Y-сomponent grayscale layer of image;
    :param U: array of U-сomponent grayscale layer of image
    :param V: array of V-сomponent grayscale layer of image
    :return: array RGB-format of image.
    '''
    transform_list = []

    for y_list, u_list, v_list in zip(Y, U, V):
        transform_list_internal = []
        for y_list_internal, u_list_internal, v_list_internal in zip(y_list, u_list, v_list):
            R = round(y_list_internal + 1.3707 * (v_list_internal - 128), 1)
            G = round(y_list_internal - 0.3365 * (u_list_internal - 128) - 0.6982*(v_list_internal - 128), 1)
            B = round(y_list_internal + 1.7324 * (u_list_internal - 128), 1)
            transform_list_internal_three_value = [R, G, B]
            transform_list_internal.append(transform_list_internal_three_value)
        transform_list.append(transform_list_internal)
    return transform_list


def transform_coefficients_from_yuv_to_rgb(Y, U, V):

    transform_list = []

    for list_of_tuples in list(zip(Y, U, V)):
        for list_of_three_lists in list_of_tuples:
            transform_list_internal = []
            zip_lists = list(zip(list_of_three_lists[0], list_of_three_lists[1], list_of_three_lists[2]))
            for three_value in zip_lists:
                R = three_value[0] + 1.3707 * (three_value[2] - 128)
                G = three_value[0] - 0.3365 * (three_value[1] - 128) - 0.6982 * (three_value[2] - 128)
                B = three_value[0] + 1.7324 * (three_value[1] - 128)
                transform_list_internal_three_value = [R, G, B]
                transform_list_internal.append(transform_list_internal_three_value)
            transform_list.append(transform_list_internal)
    return transform_list







#print(transform_coeff(get_image_array('temp.jpg'), 0.299, 0.587, 0.114)[2])


#def transformation_image_to_YUV(image):

#print(get_image_array('temp.jpg'))

#transform_coefficients_from_rgb_to_yuv(get_image_array('temp.jpg'), 0.299, 0.587, 0.114)