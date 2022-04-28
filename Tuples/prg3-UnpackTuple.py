'''
@Author: Sai Tarun
@Date: 2022-04-20 16: 05: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 16: 15: 00
@Title: Unpack tuple a tuple in several variables.
'''
tuple = 1,2,3
def unpack_tuple():
    n1,n2,n3 = tuple #Save the values from tuple into variables
    return n1+n2+n3

if __name__ == '__main__':
    print("Tuple got unpacked :",unpack_tuple()) 
