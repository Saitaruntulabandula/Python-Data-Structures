'''
@Author: Sai Tarun
@Date: 2022-04-19 18: 55: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 19: 20: 00
@Title: Difference between 2 lists.
'''
from itertools import *
#Python’s Itertool is a module that provides various functions that work on iterators to produce complex iterators. 
#This module works as a fast, memory-efficient tool that is used either by themselves or in combination to form iterator algebra. 

list1 = [64, 28, 75, 96, 48, 19, 4, 55]
list2 = [158, 63, 175, 126, 456, 250, 440, 8]

def diff_list():
    list = [(list2[x] - list1[x]) for x in range(len(list2))]
    print(list)

if __name__ == '__main__':
    diff_list()