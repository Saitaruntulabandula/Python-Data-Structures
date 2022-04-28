'''
@Author: Sai Tarun
@Date: 2022-04-21 13: 00: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 13: 25: 00
@Title: Sequence of squared vales in dictionary value.
'''  
dict={}

def squared_sequence():
    size=int(input("Enter the size of the dictionary:"))
    print("Dictionary with required sequence squared values is :")
    for i in range(1,size+1):
        key=i
        value=i*i
        dict[key]=value
        dict.update(dict)
    print(dict)

if __name__ == '__main__':
    squared_sequence()