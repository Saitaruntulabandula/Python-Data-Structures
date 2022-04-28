'''
@Author: Sai Tarun
@Date: 2022-04-19 18: 05: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 18: 20: 00
@Title: Clone or Copy a list.
'''
def clone_list():
    list = [1,2,2,3,6,3,9,5,4,0,7,3,8,10,4]
    list1 = []
    for i in range(len(list)) :
        list1.append(list[i])
    return list1

if __name__ == '__main__':
    print(clone_list())