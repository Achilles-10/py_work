def merge_ascend(left, right):
	i, j = 0, 0
	result = []
	while i < len(left) and j < len(right):
		if left[i] <= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result


def merge_sort_ascend(lists):
	if len(lists) <= 1:
		return lists
	num = int(len(lists) / 2)
	left = merge_sort_ascend(lists[:num])
	right = merge_sort_ascend(lists[num:])
	return merge_ascend(left, right)


def merge_descend(left, right):
	i, j = 0, 0
	result = []
	while i < len(left) and j < len(right):
		if left[i] >= right[j]:
			result.append(left[i])
			i += 1
		else:
			result.append(right[j])
			j += 1
	result += left[i:]
	result += right[j:]
	return result


def merge_sort_descend(lists):
	if len(lists) <= 1:
		return lists
	num = int(len(lists) / 2)
	left = merge_sort_descend(lists[:num])
	right = merge_sort_descend(lists[num:])
	return merge_descend(left, right)
