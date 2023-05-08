#!/usr/bin/python3

import sys

string = "and that piece of art is useful - Dora Korpar, 2015-10-19\n"
sys.stderr.write(string)
sys.exit(1)

# this could also be written like this sys.stderr.write('and that piece of art is useful - Dora Korpar, 2015-10-19\n'), no need to use the message as a variable that stores the string
