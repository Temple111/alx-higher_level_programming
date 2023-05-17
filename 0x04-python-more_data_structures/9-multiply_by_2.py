#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nw_dr = a_dictionary.copy()
    numb_keys = list(nw_dr.keys())

    for z in numb_keys:
        nw_dr[z] *= 2

    return (nw_dr)
