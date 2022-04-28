'''
@Author: Sai Tarun
@Date: 2022-04-21 16: 45: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 17: 10: 00
@Title: Check existence of multiple keys.
''' 
dictionary={1:"Ball",2:"Cat",3:"Apple",4:"Pink",5:"Game"}

def check_existnece():
    print(dictionary.keys() >= {1,2})
    print(dictionary.keys() >= {3,1})
    print(dictionary.keys() >= {2,4})
    print(dictionary.keys() >= {4,6})

if __name__ == '__main__':
    check_existnece()

