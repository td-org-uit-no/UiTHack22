#!/usr/bin/python
from random import *
from collections import Counter

def generate(x, y, flag):
    result_list = []
    for c in flag:
        for _ in range(100, 1000):
            n = randint(x,y)
            i = chr(n)
            if i not in flag:
                result_list.append(i)
        result_list.append(c)
    return result_list
           
if __name__ == '__main__':

    string = 'UiTHack22{Luke_would_Have_remembered_The_Password}'
    x = 33
    y = 64
    
    print(generate(x,y,string))
    
