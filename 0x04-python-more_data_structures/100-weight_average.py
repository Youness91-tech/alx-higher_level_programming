#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    weight_sum = 0
    total = 0
    for weight in my_list:
        total += weight[0] * weight[1]
        weight_sum += weight[1]
    return (total / weight_sum)
