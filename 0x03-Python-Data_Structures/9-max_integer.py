#!/usr/bin/python3
# 9-max_integer.py


def max_integer(my_list=[]):

    if len(my_list) == 0:
        return (None)

    big_int = my_list[0]
    for z in range(len(my_list)):
        if my_list[z] > big_int:
            big_int = my_list[z]

    return (big_int)
