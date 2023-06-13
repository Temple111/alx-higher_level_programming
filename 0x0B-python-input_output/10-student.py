#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, ats=None):
        if type(ats) is list:
            dc = {}
            for z in ats:
                if type(z) is not str:
                    return self.__dict__
                for a in self.__dict__:
                    if z == a:
                        dc[z] = self.__dict__[a]
            return dc
        return self.__dict__

    def reload_from_json(self, json):
        return self.__dict__.update(json)
