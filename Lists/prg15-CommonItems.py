'''
@Author: Sai Tarun
@Date: 2022-04-19 18: 55: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 19: 20: 00
@Title: Print common items in the lists.
'''

list1 = [8,1,5,2,7,4,3,9,0,6]
list2 = [2,16,11,19,13,15,12]

def common_items():
    common_list = [(x) for x in list1 for y in list2 if x == y]
    print(common_list)



if __name__ == '__main__':
    common_items()