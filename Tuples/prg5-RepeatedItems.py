'''
@Author: Sai Tarun
@Date: 2022-04-20 16: 20: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 16: 40: 00
@Title: Repeated items in the list.
'''

tuple = 1,2,3,1,2,3,4,5
list = []
def repeated_item():
    for i in range(len(tuple)) :
        count = tuple.count(tuple[i])
        if count > 1 :
            if tuple[i] not in list :
                list.append(tuple[i])
    return list

if __name__ == '__main__':
    print("Repeated items list is",repeated_item())