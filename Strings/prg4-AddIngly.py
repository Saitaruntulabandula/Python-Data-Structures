'''
@Author: Sai Tarun
@Date: 2022-04-20 21: 15: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 21: 40: 00
@Title: Adding ing or ly.
'''  
def add_ing_ly():
    string = input("Enter a string : ")
    if len(string) >= 3 :
        if string[len(string)-3:] =="ing" :
            string = string + "ly"
            return string
        else :
            string = string + "ing"
            return string
    else :
        return string

if __name__ == '__main__':
    print("String after adding ing or ly is:",add_ing_ly())