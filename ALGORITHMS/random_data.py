import random


def get_random_data(num, limit):
	_list = []
	i = 0
	while i < num:
		_list.append(random.randint(0, limit))
		i += 1
	return _list