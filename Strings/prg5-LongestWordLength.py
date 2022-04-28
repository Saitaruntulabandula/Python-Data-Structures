'''
@Author: Sai Tarun
@Date: 2022-04-20 21: 15: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-20 21: 40: 00
@Title: Longest word.
'''  
list = ["one", "two", "third", "four"]

def list_of_word_function():
    lenght = len(list[0])
    word = list[0]
    for i in list:
        if(len(i) > lenght):
            lenght = len(i)
            word = i
    print("The longest length word is '",word,
          "' and its length is",lenght)

if __name__ == '__main__':
    list_of_word_function()
