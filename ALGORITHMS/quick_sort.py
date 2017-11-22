def qucik_sort_ascend(list, left, right):
	if left >= right:
		return list
	key = list[left]
	low, high = left, right
	while left < right:
		while left < right and list[right] >= key:
			right -= 1
		list[left] = list[right]
		while left < right and list[left] < key:
			left += 1
		list[right] = list[left]
		list[left] = key
	qucik_sort_ascend(list, low, left - 1)
	qucik_sort_ascend(list, left + 1, high)
	return list

def qucik_sort_descend(list,left,right):
	if left >= right:
		return list
	key = list[right]
	low, high = left, right
	while left < right:
		while left < right and list[left] >= key:
			left += 1
		list[right] = list[left]
		while left < right and list[right] < key:
			right -= 1
		list[left] = list[right]
		list[right] = key
	qucik_sort_descend(list, low, left - 1)
	qucik_sort_descend(list, left + 1, high)
	return list