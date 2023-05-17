#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    count = 0
    dn = 0

    for z in my_list:
        count += z[0] * z[1]
        dn += z[1]

    return (count / dn)
