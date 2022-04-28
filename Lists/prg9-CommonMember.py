'''
@Author: Sai Tarun
@Date: 2022-04-19 18: 55: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 19: 20: 00
@Title: Returns True if lists had common member.
'''

list = [1, 2, 3, 4]
new_list = [0, "Akanksha", 6]
    
def common_member():
    for i in list:
        if i in new_list:
            return True
        else:
            return False
            
if __name__ == '__main__':
    print(common_member())