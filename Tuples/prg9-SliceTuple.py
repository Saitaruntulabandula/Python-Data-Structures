'''
@Author: Sai Tarun
@Date: 2022-04-20 18: 40: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 18: 45: 00
@Title: Slice tuple.
'''

tuple = 0,1,2,3,4,5,6,7,8,9,10,11,12
def slice_tuple():
    start = int(input("Enter the starting position:"))
    end=int(input("Enter the ending position:"))
    new_tuple = tuple[start:end]
    return new_tuple

if __name__ == '__main__':
    print("Tuple after slicing it is:",slice_tuple())