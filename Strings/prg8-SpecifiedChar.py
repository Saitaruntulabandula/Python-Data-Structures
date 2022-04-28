'''
@Author: Sai Tarun
@Date: 2022-04-20 22: 35: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 22: 50: 00
@Title: Last part of the string before specified character.
'''  

def specified_char():
    string = input("Enter a string : ")
    character = input("Enter a character : ")
    index = string.find(character)
    return string[:index]

if __name__ == '__main__':
    print("Last part of the string before given specified charcter is:",specified_char())