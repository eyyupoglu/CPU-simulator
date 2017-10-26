import numpy as np
import math
import decimal


def dataLoad(filename):
    i=0
    return_array=[]
    with open(filename+".txt") as f:
        for every in f:
            data = every


            words=data.split(' ')


            print(words[0], words[1], words[2])

            if float(words[0]) > 60 or float(words[0]) <10 :
                print("error in temperature for the line",i,"\n")
            if float(words[1]) <0 :
                print("error in Growth rate for the line",i,"\n")
            if not (words[2] == '1\n' or words[2]=='2\n' or words[2]=='3\n' or words[2]=='4\n') :
                print("error in Bacteria type for the line",i,"\n")



            i=i+1






    return data

print(dataLoad("test"))