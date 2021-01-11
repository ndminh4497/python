def count_number(minh):
	minh = [1,4,5,8,4,6]
	count = minh.count(4)
	return count

def list_count_4(nums):
	count = 0
	for num in nums:
		if num == 4:
			count = count + 1

	return count		


print(count_number(4))

print(list_count_4([1,5,6,7,84,5,5,4]))