'''
@Author: Sai Tarun
@Date: 2022-04-19 15: 50: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 16: 30: 00
@Title: Count number of string's.
'''
list = ['sravs' , "sai's" , 'kaple', 'adda', 'tarun']
def no_of_strings():
    count = 0
    for i in range(len(list)) :
        size_ele = len(list[i]) - 1   #for last character index.
        if len(list[i]) > 2 :         #length of the string is 2 or more.
              if (list[i][0] == list[i][size_ele]): #Check if 1st and last character's are equal.                              
                   print(list[i])
                   count+=1
    return count

if __name__ == '__main__':
    count=no_of_strings()
    print("Number of strings are:",count)
