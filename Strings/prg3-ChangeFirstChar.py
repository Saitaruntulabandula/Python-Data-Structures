'''
@Author: Sai Tarun
@Date: 2022-04-20 20: 45: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 21: 10: 00
@Title: Replace first char letter in whole string.
'''  

def replace_first_char():
    string = input("Enter a string : ")
    char=string[0]
    string=string.replace(char,"$")
    string=char+string[1:]
    return string

if __name__ == '__main__':
    print("String after replacing first char with $ is:",replace_first_char())

