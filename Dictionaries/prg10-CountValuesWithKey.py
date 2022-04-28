'''
@Author: Sai Tarun
@Date: 2022-04-21 15: 45: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 16: 20: 00
@Title: Count values with the key.
''' 
#Expected result: Count of how many dictionaries have success as True
dict1 = {'id': 1, 'success': True, 'name': 'Sai'}
dict2 = {'id': 2, 'success': False, 'name': 'Tarun'}
dict3 = {'id': 3, 'success': True, 'name': 'Raj'}

data = [dict1, dict2, dict3]

def count_with_value():
    count = 0
    for dict in data:
        if dict['success'] == True:
            count+=1
    print(count,"dictionaries had 'success' as 'True'.")

if __name__ == '__main__':
    count_with_value()
