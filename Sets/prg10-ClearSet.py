'''
@Author: Sai Tarun
@Date: 2022-04-22 13: 15: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-22 13: 20: 00
@Title: Clear the set.
'''
set1=set([1,2,3,4,5])
def clear_set_fun():
    set1.clear()
    print("Set after clearing:",set1)

if __name__=="__main__":
    clear_set_fun()