'''
@Author: Sai Tarun
@Date: 2022-04-22 11: 10: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-22 11: 20: 00
@Title: Iterate set.
'''
new_set=set()
def iterate_set():
    n=int(input("Enter the size of the set:"))
    for i in range(n):
        value=int(input("Enter the value:"))
        new_set.add(value)
    print("Values in the set are:")
    for i in new_set:
        print(i)
    print(new_set)

if __name__=="__main__":
    iterate_set()