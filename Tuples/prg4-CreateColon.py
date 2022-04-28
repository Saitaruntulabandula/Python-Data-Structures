'''
@Author: Sai Tarun
@Date: 2022-04-20 16: 05: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 16: 15: 00
@Title: Create colon of a tuple.
'''
from copy import  deepcopy
tuple = 1,2,3,4

def create_colon():
    tuple1 = deepcopy(tuple)
    return tuple1

if __name__ == '__main__':
    print("colon of the tuple is :",create_colon()) 