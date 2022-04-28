'''
@Author: Sai Tarun
@Date: 2022-04-21 14: 35: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 15: 10: 00
@Title: Dictionary from the string.
''' 
dictionary={}

def dict_from_string():
    new_string=input("Enter the string:")
    for i in range(len(new_string)):
        key=i
        value=new_string[i]
        dictionary[key]=value
        dictionary.update(dictionary)
    print(dictionary)

if __name__ == '__main__':
    dict_from_string()