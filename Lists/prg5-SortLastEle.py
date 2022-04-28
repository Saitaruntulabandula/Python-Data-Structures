'''
@Author: Sai Tarun
@Date: 2022-04-19 16: 50: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 17: 30: 00
@Title: Sorted list with the last element in the tuple.
'''
def list(n):
    return n[-1] #getting the last key
def sort_list(tuples):
	return sorted(tuples, key=list)

if __name__ == '__main__':
    print(sort_list([(2,5),(1,2),(4,4),(2,3),(2,1)]))