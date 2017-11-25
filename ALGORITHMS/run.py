from insertion_sort import *
from bubble_sort import *
from selection_sort import *
from merge_sort import *
from quick_sort import *
from random_data import get_random_data

list_1 = get_random_data(10,100)
insertion_sort_ascend(list_1)
print ("The result after insertion sort is: " + str(list_1))

list_2 = get_random_data(10,100)
list_2 = merge_sort_ascend(list_2)
print ("\nThe result after merge sort is: " + str(list_2))

list_3 = get_random_data(10,100)
bubble_sort_ascend(list_3)
print ("\nThe result after bubble sort is: " + str(list_3))

list_4 = get_random_data(10,100)
selection_sort_ascend(list_4)
print ("\nThe result after selection sort is: " + str(list_4))

list_5 = get_random_data(10,100)
qucik_sort_ascend(list_5,0,9)
print ("\nThe result after quick sort is: " + str(list_5))