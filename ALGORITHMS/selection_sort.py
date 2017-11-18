def selection_sort_ascend(list):
	for j in range(0, len(list)):
		min = j
		for i in range(j + 1, len(list)):
			if list[i] < list[min]:
				min = i
			i += 1
		list[min], list[j] = list[j], list[min]
	return list


def selection_sort_descend(list):
	for j in range(0, len(list)):
		max = j
		for i in range(j + 1, len(list)):
			if list[i] > list[max]:
				max = i
			i += 1
		list[max], list[j] = list[j], list[max]
	return list
