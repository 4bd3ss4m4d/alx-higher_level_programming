#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return 0
    sum = 0
    div = 0
    for tup in my_list:
        sum += tup[0] * tup[1]
        div += tup[1]
    return sum / div
