'''
@Author: Sai Tarun
@Date: 2022-04-20 17: 20: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 17: 40: 00
@Title: Program to convert list to tuple.
'''
list = [1,2,3,4,5]

def list_tuple():
    final_tuple = tuple(list)
    return final_tuple
if __name__ == '__main__':
    print("List after converting into tuple is:",list_tuple())