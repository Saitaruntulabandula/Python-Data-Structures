'''
@Author: Sai Tarun
@Date: 2022-04-21 13: 30: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 13: 50: 00
@Title: Remove key from the dictionary.
''' 
dictionary={1:"Ball",2:"Cat",3:"Apple",4:"Pink",5:"Game"}

def remove_key():
    key=int(input("Enter the key which you want to remove:"))
    dictionary.pop(key)
    print("Dictionary after removing the given key is",dictionary)

if __name__ == '__main__':
    remove_key()
