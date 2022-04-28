'''
@Author: Sai Tarun
@Date: 2022-04-20 18: 46: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 18: 57: 00
@Title: Reverse Tuple.
'''

tuple = 0,1,2,3,4,5,6,7,8,9,10,11,12
list=[]
def reverse_tuple():
    length = len(tuple)-1
    while length >= 0 :
        temp = tuple[length]
        list.append(temp)
        length-=1
    return list

if __name__ == '__main__':
    print("Tuple after reversing it:",reverse_tuple())