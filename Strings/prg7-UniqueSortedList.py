'''
@Author: Sai Tarun
@Date: 2022-04-20 21: 50: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 22: 30: 00
@Title: Unique sorted list.
'''  
list=["red","white","black","pink","red","green","black","yellow","pink"]
unique_list=[]
unique_sorted_list=[]
def unique_soreted_list():
    for i in range(len(list)):
        if list[i] not in unique_list:
            unique_list.append(list[i])
    unique_soreted_list=sorted(unique_list)
    return unique_soreted_list

if __name__ == '__main__':
    print("Sorted list with unique items is:",unique_soreted_list())