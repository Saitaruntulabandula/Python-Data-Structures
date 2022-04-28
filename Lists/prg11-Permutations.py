'''
@Author: Sai Tarun
@Date: 2022-04-19 18: 55: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 19: 20: 00
@Title: Permutations of the list.
'''
input_list = [1,2,3,4]
def per(list):
    if len(list) == 0:
        return []

    if len(list) == 1:
        return [list]

    list2 = []

    for i in range(len(list)):
        temp1 = list[i]                       #ele1 #range0-0th index
        temp2 = list[:i] + list[i + 1:]       #all ele(not ele1)

        for p in per(temp2):
            list2.append([temp1] + p)
    return list2

if __name__ == '__main__':
    for p in per(input_list):
        print(p)