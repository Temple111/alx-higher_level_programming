#!/usr/bin/python3
for figure in range(0, 100):
    if figure == 99:
        print("{}".format(figure))
    else:
        print("{:02d}".format(figure), end=", ")
