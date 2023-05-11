#!/usr/bin/python3
import sys


if __name__ == "__main__":

    av = sys.argv
    list_size = len(av) - 1

    if list_size > 1:
        print("{} arguments:".format(list_size))
        for a in range(1, list_size + 1):
            print("{}: {}".format(a, av[a]))

    elif list_size == 0:
        print("{} arguments.".format(size))

    else:
        print("{} argument:".format(list_size))
        print("{}: {}".format(list_size, av[1]))
