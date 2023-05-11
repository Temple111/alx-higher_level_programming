#!/usr/bin/python3

def magic_calculation(a, b):
    
    from magic_calculation_102 import add, sub

    if a < b:
        z = add(a, b)
        for v in range(4, 6):
            z = add(z, v)
        return (z)

    else:
        return(sub(a, b))
