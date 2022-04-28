'''
@Author: Sai Tarun
@Date: 2022-04-21 13: 55: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 14: 30: 00
@Title: Unique values.
''' 

dictionary={}

def unique_values():
    size=int(input("Enter the size of the dictionary:"))
    for i in range(size):
        key=int(input("Enter the key:"))
        value=int(input("Enter the value:"))
        dictionary[key]=value
        dictionary.update(dictionary)    
    new_set=set(dictionary.values())
    print("Dictionary with unique values is:")
    print(new_set)

if __name__ == '__main__':
    unique_values()