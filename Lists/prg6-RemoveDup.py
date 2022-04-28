'''
@Author: Sai Tarun
@Date: 2022-04-19 17: 35: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 17: 50: 00
@Title: Remove duplicates from list.
'''
def remove_duplicates():
    list = [1,2,2,3,6,3,9,5,4,0,7,3,8,10,4]
    list1 = []
    for i in list : 
        if i not in list1 : # If list1 doesn't contain the element append it
            list1.append(i)
    return list1

if __name__ == '__main__':
    print(remove_duplicates())