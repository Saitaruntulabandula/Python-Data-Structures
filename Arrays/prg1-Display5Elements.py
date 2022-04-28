'''
@Author: Sai Tarun
@Date: 2022-04-22 14: 20: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-22 14: 35: 00
@Title: Printing array elements using indexing.
'''
from array import *
new_array=array("i",[1,2,3,4,5])
def array_index(): 
    print("Array of elements using indexing are:")
    for i in range(len(new_array)):
        print(new_array[i])

if __name__=="__main__":
    array_index()