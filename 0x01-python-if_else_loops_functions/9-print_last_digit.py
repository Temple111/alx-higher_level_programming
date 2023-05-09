#!/usr/bin/python3


def print_last_digit(number):
    Last_Num = (number % 10) if number >= 0 else ((number * -1) % 10)
    print(Last_Num, end='')
    return (Last_Num)
