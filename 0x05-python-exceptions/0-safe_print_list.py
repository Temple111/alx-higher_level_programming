#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    all_ = 0
    for z in range(x):
        try:
            print("{}".format(my_list[z]), end="")
            all_ += 1
        except IndexError:
            break
    print("")
    return (all_)
