#!/usr/bin/python3
from json import loads


def load_from_json_file(filename):
    with open(filename, 'r') as k:
        return loads(k.read())
