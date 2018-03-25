import scipy.io
import numpy
import pywt
import matplotlib.pyplot as plot
#import main

#image = main.get_image_array('temp.jpg')

#print(image)


a = [[1, 2, 3], [10, 15, 17], [0, 1, 0]]

b = [[4, 5, 6], [5, 4, 3], [2, 2, 2]]

c = [[1, 1, 1], [7, 7, 7], [6, 6, 6]]

result = list(zip(a, b, c))

print(result)
print(list(zip(result[0][0], result[0][1], result[0][2])))


# for list_of_tuples in list(zip(a, b, c)):
#     for list_of_three_lists in list_of_tuples:
#         zip_lists = list(zip(list_of_three_lists[0], list_of_three_lists[1], list_of_three_lists[2]))
#         for three_value in zip_lists:
#
#
#
#
# print(list_of_three_list)





'''
result = [ [[r, g, b], ..., [r, g, b]],...,[[r, g, b], ..., [r, g, b]] ]
'''


