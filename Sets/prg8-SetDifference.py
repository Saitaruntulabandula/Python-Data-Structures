'''
@Author: Sai Tarun
@Date: 2022-04-22 12: 45: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-22 12: 50: 00
@Title: Difference of the set.
'''
set1=set([1,2,3,4,5])
set2=set([9,8,7,6,5])
def difference_fun():
    print("Difference of the given sets are:",set1.difference(set2))

if __name__=="__main__":
    difference_fun()