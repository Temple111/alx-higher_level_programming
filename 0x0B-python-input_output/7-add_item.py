#!/usr/bin/python3
from sys import argv
from os import path
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


x = []
if path.exists("add_item.json"):
    x = load_from_json_file("add_item.json")
x = x + argv[1:]
save_to_json_file(x, "add_item.json")
