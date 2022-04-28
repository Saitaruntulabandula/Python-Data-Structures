'''
@Author: Sai Tarun
@Date: 2022-04-20 16: 45: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 17: 10: 00
@Title: Checking weather the element is exist or not.
'''
tuplex = ("w", "a", "r", "e", "s", "o", "u", "r", "c", "e")
def check_existence():
    value="n" in tuplex
    return value

if __name__ == '__main__':
    if check_existence()==True:
        print("Element is Present")
    else:
        print("Element is Not Present")
