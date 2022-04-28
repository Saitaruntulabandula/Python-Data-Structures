'''
@Author: Sai Tarun
@Date: 2022-04-21 16: 25: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 16: 40: 00
@Title: Convert list into a nested dictionary of keys.
''' 
num_list = [1, 2, 3, 4]

def list_nested_dict():
    new_dict = current = {}
    for name in num_list:
        current[name] = {}
        current = current[name]
    print("Newly created nested dictionary from the given list of elements is:")
    print(new_dict)

if __name__ == '__main__':
    list_nested_dict()