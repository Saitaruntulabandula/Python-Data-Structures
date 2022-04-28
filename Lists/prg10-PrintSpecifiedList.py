'''
@Author: Sai Tarun
@Date: 2022-04-19 18: 55: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 19: 20: 00
@Title: Print specified list.
'''
def specified_list():
    list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    element1 = list[0]
    element2 = list[4]
    element3 = list[5]
    list.remove(element1)
    list.remove(element2)
    list.remove(element3)
    return list
    
if __name__ == '__main__':
    print(specified_list())