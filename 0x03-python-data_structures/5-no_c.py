#!/usr/bin/python3
# 5-no_c.py


def no_c(my_string):

    remove_copy = [z for z in my_string if z != 'c' and z != 'C']
    return ("".join(remove_copy))
