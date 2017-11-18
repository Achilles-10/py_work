def insertion_sort_ascend(list):
	for j in range(0, len(list)):
		key = list[j]
		i = j - 1
		while i >= 0:
			if list[i] > key:
				list[i + 1] = list[i]
				list[i] = key
			i -= 1
	return list


def insertion_sort_descend(list):
	for j in range(0, len(list)):
		key = list[j]
		i = j - 1
		while i >= 0:
			if list[i] < key:
				list[i + 1] = list[i]
				list[i] = key
			i -= 1
	return list
