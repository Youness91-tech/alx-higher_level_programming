#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq_list = set(my_list)
    rslt = 0
    for num in uniq_list:
        rslt += num
    return rslt
