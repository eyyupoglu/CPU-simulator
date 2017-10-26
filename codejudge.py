import numpy as np
import math
import decimal


def dataLoad(filename):

    with open(filename+".txt") as f:

        new_data=np.array([0,0,0])
        for a_line in f:
            word = a_line.split(' ')
            data = np.array([float(word[0]),float(word[1]),float(word[0])])

            new_data = np.vstack((new_data,data))

    data = new_data

    new_array = np.array([0, 0, 0])
    number_of_rows = data.shape[0]
    for i in range(number_of_rows):
        if data[i][0] < 10 or data[i][0] > 60:

            print("error type: temperature in line", i)
        if data[i][1] < 0:

            print("error type:  growth rate in line", i)
            print(data[i])
        else:
            new_array = np.vstack((new_array, data[i]))

    return new_array

print(dataLoad("test"))