'''
@Author: Sai Tarun
@Date: 2022-04-21 15: 15: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 15: 40: 00
@Title: Dictionary in table format.
''' 
dictionary={1:"Ball",2:"Cat",3:"Apple",4:"Pink",5:"Game"}

def table_format():
    print("Given dictionary in table format is:")
    for key,vlaue in dictionary.items():
        print(key,vlaue)

if __name__ == '__main__':
    table_format()