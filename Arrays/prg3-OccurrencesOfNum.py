'''
@Author: Sai Tarun
@Date: 2022-04-22 15: 10: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-22 15: 30: 00
@Title: Occurrence of a element.
'''
from array import *

new_array=array("i",[1,2,3,4,5,1,7,2,4,2])

def element_occurrence(): 
    count=0
    element=int(input("Enter the element which you want to check:"))
    for i in range(len(new_array)):
        if element==new_array[i]:
            count+=1
    print("The element",element,"occurred",count,"times")


if __name__=="__main__":
    element_occurrence()