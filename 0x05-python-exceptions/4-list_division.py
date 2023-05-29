#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    ele_list = []
    for o in range(0, list_length):
        try:
            divi = my_list_1[o] / my_list_2[o]
        except TypeError:
            print("wrong type")
            divi = 0
        except ZeroDivisionError:
            print("division by 0")
            divi = 0
        except IndexError:
            print("out of range")
            divi = 0
        finally:
            ele_list.append(divi)
    return (ele_list)
