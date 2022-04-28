'''
@Author: Sai Tarun
@Date: 2022-04-19 18: 55: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 19: 20: 00
@Title: Append new list to existing list.
'''

list1 = [8,1,5,7,4,3,9,0,6]
list2 = [2,16,11,19,13,15,12]

def append_list():
    for i in range(len(list2)) :
        list1.append(list2[i])
    print(list1)

if __name__ == '__main__':
    append_list()