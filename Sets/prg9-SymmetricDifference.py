'''
@Author: Sai Tarun
@Date: 2022-04-22 12: 55: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-22 13: 10: 00
@Title: Symmetric difference of the set.
'''
set1=set([1,2,3,4,5])
set2=set([9,8,7,6,5])
def symmetric_difference_fun():
    print("Difference of the given sets are:",set1.symmetric_difference(set2))

if __name__=="__main__":
    symmetric_difference_fun()