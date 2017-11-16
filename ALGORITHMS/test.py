from insertion_sort import *
from random_data import get_random_data

list = get_random_data(10, 100)
list = insertion_sort_descend(list)
print(list)
list = insertion_sort_ascend(list)
print(list)
