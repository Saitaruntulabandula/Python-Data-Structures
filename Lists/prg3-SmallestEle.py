'''
@Author: Sai Tarun
@Date: 2022-04-19 15: 05: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 15: 30: 00
@Title: Smallest element in the list.
'''
def user_input():
    n=int(input("Enter the range: "))
    list=[]
    for i in range(n):
        list.append(int(input("Enter the element: ")))
    return list

def smallest_number():
    new_list=user_input()
    smallest = new_list[0]
    for i in new_list:
        if i<smallest:
            smallest=i
    return smallest

if __name__ == '__main__':
    smallest=smallest_number()
    print("Smallest element is: ", smallest)