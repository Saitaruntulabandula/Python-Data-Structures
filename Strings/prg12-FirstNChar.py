'''
@Author: Sai Tarun
@Date: 2022-04-21 00: 30: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 00: 40: 00
@Title: Lower case first n chars.
'''

from operator import index


def first_n_char():
    string=input("Enter the string: ")
    index=int(input("Enter the location:"))
    return string[:index].lower()

if __name__ == '__main__':
    print("First n chars after lower casing is:",first_n_char())