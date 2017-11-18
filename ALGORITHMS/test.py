from insertion_sort import *
from bubble_sort import *
from selection_sort import *
from merge_sort import *
from random_data import get_random_data

list = get_random_data(10, 100)
list = bubble_sort_descend(list)
print (list)