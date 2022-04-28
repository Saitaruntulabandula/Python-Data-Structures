'''
@Author: Sai Tarun
@Date: 2022-04-20 22: 55: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 23: 20: 00
@Title: specified width.
'''  
import textwrap

def specified_width():
    string = input("Enter the string:")
    return textwrap.fill(string, width=50)

if __name__ == '__main__':
    print("String with width 50 is: ",specified_width())