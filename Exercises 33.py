def sum_of_three(a,b,c):
	if (a == b or a == c or b == c):
		sum = 0
		return sum
	else:
		sum = a + b + c
		return sum

print(sum_of_three(2, 1, 2))
print(sum_of_three(3, 2, 2))
print(sum_of_three(2, 2, 2))
print(sum_of_three(1, 2, 3))	