'''
@Author: Sai Tarun
@Date: 2022-04-19 18: 55: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-19 19: 20: 00
@Title: Split list based on first character.
'''

from itertools import *
from operator import *

list = ["Sai", "Bharat", "Sravya", "Kevin","Bhanu"]
list2 = []

def split_words():
    for letter,word in groupby(sorted(list), key=itemgetter(0)) :
        #It print the values such that the first alphabet becomes the key
        #and by using sorted() it'll group the elements with same 1st alphabet.
        print(letter)
        for i in word :
            print(i)

if __name__ == '__main__':
    split_words()