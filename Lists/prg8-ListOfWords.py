'''
@Author: Sai Tarun
@Date: 2022-04-19 18: 30: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 18: 50: 00
@Title: Display the words whose lenght is more then n.
'''

list = ["Saitarun","Tulabandula", "Nandakumar", "Raj", "Kumar"]
def check_length():
    length = int(input("Enter the length of the string : "))
    for i in range(len(list)) :
        if len(list[i]) > length :
            print(list[i])
    
if __name__ == '__main__':
    check_length()    