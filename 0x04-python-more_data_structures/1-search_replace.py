#!/usr/bin/python3
def search_replace(my_list, search, replace):
    nw_lt = list(map(lambda z: replace if z == search else z, my_list))
    return (nw_lt)
