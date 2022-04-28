'''
@Author: Sai Tarun
@Date: 2022-04-22 11: 45: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-22 12: 10: 00
@Title: Remove members.
'''
new_set=set()
def add_members():
    n=int(input("Enter the size of the set:"))
    for i in range(n):
        value=int(input("Enter the value :"))
        new_set.add(value)
    print(new_set)
    remove_value=int(input("Enter the value which you want to remove:"))
    new_set.remove(remove_value)
    return new_set

if __name__=="__main__":
    print("Set after removing members is",add_members())