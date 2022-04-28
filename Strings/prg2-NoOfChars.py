'''
@Author: Sai Tarun
@Date: 2022-04-20 20: 20: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 20: 40: 00
@Title: Number of characters.
'''
dict = {}
def no_of_characters():
    string = input("Enter the string : ")
    for i in range(len(string)) :
        key = string.count(string[i])
        dict[string[i]] = key
    return dict

if __name__ == '__main__':
    print("Number of characters are:",no_of_characters())
