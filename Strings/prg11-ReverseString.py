'''
@Author: Sai Tarun
@Date: 2022-04-20 23: 50: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 00: 10: 00
@Title: Reverse the given string.
'''

def reverse_string():
    string=input("Enter the string: ")
    return string[::-1]

if __name__ == '__main__':
    print("Reversed string is:",reverse_string())