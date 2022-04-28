'''
@Author: Sai Tarun
@Date: 2022-04-21 11: 35: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 11: 57: 00
@Title: Add key to the dictionary.
'''  

dict = {}
def add_key():
        num = int(input("Enter number of key value pairs you want to add in dictionary: "))
        for i in range(1,num+1) :
                input_key = input("Enter the key which you want to add to your dictionary:")
                value = i*10
                dict[input_key] = value
        print(dict)

if __name__ == '__main__':
        print("Newly created dictionary with the given keys is:",add_key())