'''
@Author: Sai Tarun
@Date: 2022-04-21 17: 15: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 17: 35: 00
@Title: Count number of items in the dictionary.
''' 
dictionary={1:"Ball",2:[1,2,3,4],3:"Apple",4:[4,3,2,1],5:[8,6,4,2]}
def count_items():
    count=0
    for value in dictionary.values():
        if type(value)==list:
            count=count+1
    print("Number of list type items in the dictionary is:",count)

if __name__ == '__main__':
    count_items()