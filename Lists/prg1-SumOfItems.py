'''
@Author: Sai Tarun
@Date: 2022-04-19 14: 09: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 14: 26: 00
@Title: Add the items in the list.
'''
def user_input():
    n=int(input("Enter the range: "))
    list=[]
    for i in range(n):
        list.append(int(input("Enter the element: ")))
    return list

def sum_of_list():
    result=0
    new_list=user_input()
    for i in range(len(new_list)):
        result=result+new_list[i]
    print("Sum of the addition of the list elements are:",result)


if __name__ == '__main__':
    sum_of_list()