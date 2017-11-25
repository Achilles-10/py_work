# 4.3
numbers = [number for number in range(1,21)]
print(numbers)

for many_number in range(1,1000001):
	print(many_number)

somany_numbers = [somany_number for somany_number in range(1,1000001)]
print(min(somany_numbers))
print(max(somany_numbers))
print(sum(somany_numbers))

odd_numbers = []
for odd_num in range(1,21,2):
	odd_numbers.append(odd_num)
print(odd_numbers)

_3numbers = []
for _3num in range(3,31,3):
	_3numbers.append(_3num)
print(_3numbers)

cubics = []
for cubic in range(1,11):
	cubics.append(cubic**3)
print(cubics)

_cubics = [cubic**3 for cubic in range(1,11)]
print(_cubics)
