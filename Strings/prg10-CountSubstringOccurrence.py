'''
@Author: Sai Tarun
@Date: 2022-04-20 23: 30: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 23: 45: 00
@Title: Count Occurrences of substring.
'''
def substring_occurrences():
    string = input("Enter the string:")
    sub_string=input("Enter the sub-string:")
    return string.count(sub_string)

if __name__ == '__main__':
    print("Count of sub string occurrence in the given string is:",substring_occurrences())