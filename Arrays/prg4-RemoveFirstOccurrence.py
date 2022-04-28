'''
@Author: Sai Tarun
@Date: 2022-04-22 15: 35: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-22 15: 50: 00
@Title: Remove first occurrence of a element.
'''
from array import *

new_array=array("i",[1,2,3,4,5,1,7,2,4,2])

def element_occurrence(): 
    element=int(input("Enter the element which you want to remove:"))
    new_array.remove(element)
    print("Array after removing specified element first occurrence is: ",new_array)
            
if __name__=="__main__":
    element_occurrence()