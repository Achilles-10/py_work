def selection_sort_ascend(list):
	for j in range(0, len(list)):
		i = j + 1
		min = j
		while i < len(list):
			if list[i] < list[min]:
				min = i
			i += 1
		list[min], list[j] = list[j], list[min]
	return list

def selection_sort_descend(list):
	for j in range(0, len(list)):
		i = j + 1
		max = j
		while i < len(list):
			if list[i] > list[max]:
				max = i
			i += 1
		list[max], list[j] = list[j], list[max]
	return list