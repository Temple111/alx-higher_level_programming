#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    ret_copy = my_list[:]
    if 0 <= idx < len(my_list):
        ret_copy[idx] = element
        return(ret_copy)
    return(my_list)
