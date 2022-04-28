'''
@Author: Sai Tarun
@Date: 2022-04-19 14: 28: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 14: 50: 00
@Title: Multiply the items in the list.
'''
def user_input():
    n=int(input("Enter the range: "))
    list=[]
    for i in range(n):
        list.append(int(input("Enter the element: ")))
    return list

def mul_of_list():
    result=1
    new_list=user_input()
    for i in range(len(new_list)):
        result=result*new_list[i]
    print(result)


if __name__ == '__main__':
    mul_of_list()