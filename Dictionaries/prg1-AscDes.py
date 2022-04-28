'''
@Author: Sai Tarun
@Date: 2022-04-21 11: 10: 00
@Last Modified by: Sai Tarun
@Last Modified time: 2022-04-21 11: 30: 00
@Title: Dictionary in Ascending and Descending order.
'''  
import operator
#iterable---Required. The sequence to sort, list, dictionary, tuple etc.
#key     ---Optional. A Function to execute to decide the order. Default is None
#reverse ---Optional. A Boolean. False will sort ascending, True will sort descending. Default is False

dictionary={1:"Ball",2:"Cat",3:"Apple",4:"Pink",5:"Game"}
def asc_dsc_order():
    #operator.itemgetter(1) will give you: A function that grabs the first item from a list-like object.
    sorted_dict=sorted(dictionary.items(),key=operator.itemgetter(1))
    print("Dictioanry in ascending order is:",sorted_dict)
    sorted_dict=sorted(dictionary.items(),key=operator.itemgetter(1),reverse=True)
    print("Dictioanry in descending order is:",sorted_dict)

if __name__ == '__main__':
   asc_dsc_order()

