'''
@Author: Sai Tarun
@Date: 2022-04-21 12: 40: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 12: 55: 00
@Title: Iterate dictionary using for loop.
'''  

dictionary={1:"Ball",2:"Cat",3:"Apple",4:"Pink",5:"Game"}

def iterate_dict():
    print("Dictionay after iterating using for loop is:")
    for key,value in dictionary.items():
        print(key,value)

if __name__ == '__main__':
    iterate_dict()
