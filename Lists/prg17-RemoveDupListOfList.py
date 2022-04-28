'''
@Author: Sai Tarun
@Date: 2022-04-19 18: 55: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 19: 20: 00
@Title: Remove duplicates from list of list.
'''
import itertools
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
print("Before removing duplicates:", num)
def remove_duplicates():
    num.sort()
    new_num = list(num for num,_ in itertools.groupby(num))
    print("After removing duplicates:", new_num)
#_ stands for variable without any name. Generally we give for i in list here we specify 
# a variable i by using i we do further process at the same we can do this process without
# assigning any name like _
if __name__ == '__main__':
    remove_duplicates()