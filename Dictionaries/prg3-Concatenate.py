'''
@Author: Sai Tarun
@Date: 2022-04-21 12: 05: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 12: 30: 00
@Title: Concatenate two dictionaries.
'''  
dict={}
dict1={}
def concatenate_dict():
    num=int(input("Enter the number of dictionaries you want to concatenate:"))
    while num>0:
        size=int(input("Enter the number of key value pairs you want in dictionary:"))
        while size>0:
            input_key=(input("Enter the key:"))
            input_value=input("Enter the value:")
            dict[input_key]=input_value
            size-=1
        num-=1
        dict.update(dict1)
    print(dict)

if __name__ == '__main__':
    print("Newly concatenated dictionary is:",concatenate_dict())