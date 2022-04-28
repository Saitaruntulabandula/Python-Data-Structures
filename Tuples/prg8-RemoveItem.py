'''
@Author: Sai Tarun
@Date: 2022-04-20 18: 00: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 18: 30: 00
@Title: Remove Item from the tuple.
'''
tuple = 1,2,3,4,5
def remove_item():
    print(tuple)
    index = int(input("Enter the index of the element to remove:"))
    new_tuple = tuple[:index] + tuple[index+1:]
    return new_tuple

if __name__ == '__main__':
    print("Tuple after removing given element is:",remove_item())