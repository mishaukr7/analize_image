import scipy.io
import numpy


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
    """
    Transform RGB format to YUV (grayscale layer format).
    :param Y: array of Y-сomponent grayscale layer of image;
    :param U: array of U-сomponent grayscale layer of image
    :param V: array of V-сomponent grayscale layer of image
    :return: array RGB-format of image.
    """
    transform_list = []

    for y_list, u_list, v_list in zip(Y, U, V):
        transform_list_internal = []
        for y_list_internal, u_list_internal, v_list_internal in zip(y_list, u_list, v_list):
            R = y_list_internal + 1.3707 * (v_list_internal - 128)
            G = y_list_internal - 0.3365 * (u_list_internal - 128) - 0.6982*(v_list_internal - 128)
            B = y_list_internal + 1.7324 * (u_list_internal - 128)
            transform_list_internal_three_value = [abs(float(R)), abs(float(G)), abs(float(B))]
            transform_list_internal.append(transform_list_internal_three_value)
        transform_list.append(list(transform_list_internal))
    return transform_list


def transform_coefficients_from_yuv_to_rgb1(Y, U, V):
    transform_list = []
    for list_of_tuples in list(zip(Y, U, V)):
        for list_of_three_lists in list_of_tuples:
            transform_list_internal = []
            zip_lists = list(zip(list_of_three_lists[0], list_of_three_lists[1], list_of_three_lists[2]))
            for first, second, third in zip_lists:
                R = first + 1.3707 * (third - 128)
                G = first - 0.3365 * (second - 128) - 0.6982 * (third - 128)
                B = first + 1.7324 * (second - 128)
                transform_list_internal_three_value = [abs(int(R)), abs(int(G)), abs(int(B))]
                transform_list_internal.append(transform_list_internal_three_value)
            transform_list.append(transform_list_internal)
    return transform_list


def transform(y, u, v):
    first_list = [x for x in y]
    second_list = [x for x in u]
    third_list = [x for x in v]
    transform_result_list = []
    for counter_external in range(len(first_list)):
        transform_internal = []
        for counter_internal in range(len(first_list[counter_external])):
            r = first_list[counter_external][counter_internal] + 1.3707 * \
                    (third_list[counter_external][counter_internal] - 128)
            g = first_list[counter_external][counter_internal] - 0.3365 * \
                    (second_list[counter_external][counter_internal] - 128) - \
                    0.6982 * (third_list[counter_external][counter_internal - 128])
            b = first_list[counter_external][counter_internal] + 1.7324 * \
                    (second_list[counter_external][counter_internal] - 128)
            three_rgb_value = [abs(float(r/255)), abs(float(g/255)), abs(float(b/255))]
            transform_internal.append(three_rgb_value)
        transform_result_list.append(transform_internal)
    return transform_result_list


def last_transform(y, u, v):
    external_array = []
    for q_1 in range(len(y)):
        internal_array = []
        for q_2 in range(len(y[q_1])):
            r = y[q_1][q_2] + 1.3707 * (v[q_1][q_2] - 128)
            g = y[q_1][q_2] - 0.3365 * (u[q_1][q_2] - 128) - 0.6982 * (v[q_1][q_2] - 128)
            b = y[q_1][q_2] + 1.7324 * (u[q_1][q_2] - 128)
            internal_array.append([r, g, b])
        external_array.append(internal_array)
    return external_array




#print(transform_coeff(get_image_array('temp.jpg'), 0.299, 0.587, 0.114)[2])


#def transformation_image_to_YUV(image):

#print(get_image_array('temp.jpg'))

#transform_coefficients_from_rgb_to_yuv(get_image_array('temp.jpg'), 0.299, 0.587, 0.114)