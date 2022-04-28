'''
@Author: Sai Tarun
@Date: 2022-04-22 13: 25: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-22 13: 40: 00
@Title: Frozen sets.
'''
#Frozensets are like sets except that they cannot be changed, i.e. they are immutable:
s={'red','black','green'} 
def frozen_set(): 
    set=frozenset(s)
    print("Frozen set is : ",set)
    set.add('blue')
    print(set)

if __name__=="__main__":
    frozen_set()