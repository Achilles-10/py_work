def bubble_sort_ascend(list):
	for i in range(0, len(list)):
		for j in range(len(list) - 1, i, -1):
			if list[j] < list[j - 1]:
				list[j], list[j - 1] = list[j - 1], list[j]
	return list


def bubble_sort_descend(list):
	for i in range(len(list) - 1, 0, -1):
		for j in range(0, i):
			if list[j] > list[j + 1]:
				list[j], list[j + 1] = list[j + 1], list[j]
	return list
