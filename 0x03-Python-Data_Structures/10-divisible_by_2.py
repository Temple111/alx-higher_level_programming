#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mult_of_2 = my_list[:]
    for increase, z in enumerate(my_list):
        if z % 2 == 0:
            mult_of_2[increase] = True
        else:
            mult_of_2[increase] = False
    return(mult_of_2)
