def sum_of_two(a,b):
	sum = a + b
	if sum in range(15,20):
		return '20'
	else:
		return sum

print(sum_of_two(10, 6))
print(sum_of_two(10, 2))
print(sum_of_two(10, 12))	