#!/usr/bin/python3
from json import dumps


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as y:
        k = dumps(my_obj)
        y.write(k)
