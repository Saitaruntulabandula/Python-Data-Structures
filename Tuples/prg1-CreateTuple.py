'''
@Author: Sai Tarun
@Date: 2022-04-20 15: 05: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 15: 30: 00
@Title: Create Tuple.
'''
list = []

def create_tuple():
    size = int(input("Enter the size :"))
    print("Enter elements :")
    for i in range(size):
        temp = input()
        list.append(temp)
    return tuple(list)

if __name__ == '__main__':
    print("New tuple is:",create_tuple())
