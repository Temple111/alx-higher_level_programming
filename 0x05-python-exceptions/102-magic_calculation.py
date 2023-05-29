#!/usr/bin/python3


def magic_calculation(a, b):
    rslt = 0
    for o in range(1, 3):
        try:
            if o > a:
                raise Exception('Too far')
            else:
                rslt = rslt + (a ** b / o)
        except Exception:
            rslt = b + a
            break
    return (rslt)
