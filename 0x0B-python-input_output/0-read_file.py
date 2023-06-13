#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, 'r') as k:
        for ia in k:
            print(ia, end="")
    k.closed
