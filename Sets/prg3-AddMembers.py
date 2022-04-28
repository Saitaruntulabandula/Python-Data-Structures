'''
@Author: Sai Tarun
@Date: 2022-04-22 11: 25: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-22 11: 40: 00
@Title: Add members.
'''
new_set=set()
def add_members():
    n=int(input("Enter the size of the set:"))
    for i in range(n):
        value=int(input("Enter the value:"))
        new_set.add(value)
    return new_set

if __name__=="__main__":
    print("Set after adding members is",add_members())

