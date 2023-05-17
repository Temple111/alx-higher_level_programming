#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    lt = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    numbs = [lt[z] for z in roman_string] + [0]
    count = 0

    for b in range(len(numbs) - 1):
        if numbs[b] >= numbs[b+1]:
            count += numbs[b]
        else:
            count -= numbs[b]

    return count
