#!/usr/bin/python
import random
from collections import Counter


def convert_to_decimal(string):

    corr_list = []
    for i in string: 
        num = ord(i)
        corr_list.append(num)
    return corr_list
        
def gen_random(x,y,string):
    sol_list = convert_to_decimal(string)
    ran_list = []
    for i in range(0,10000):
        num = random.randint(x,y)
        if num not in sol_list:   
            ran_list.append(num)

    new_list = []
    for i in ran_list: 
        i = chr(i)
        new_list.append(i)

    for j in sol_list:
        new_list.insert(random.randint(0,1000),chr(j))
  
    return new_list
           
if __name__ == '__main__':

    string = 'UiTHack22HanSolo'
    x = 33
    y = 64
    # list = gen_random(x,y,string)
    # print(list)
    # print(convert_to_decimal(string))
    # print(remove_sol(x,y,string))
    # solve(file='han_shot_first.txt')

