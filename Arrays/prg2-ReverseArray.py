'''
@Author: Sai Tarun
@Date: 2022-04-22 14: 40: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-22 14: 55: 00
@Title: Reversing the given array.
'''
from array import *

new_array=array("i",[1,2,3,4,5])
def reverse_array(): 
    new_array.reverse()
    print("Array of elements after reversing is:",new_array)

if __name__=="__main__":
    reverse_array()