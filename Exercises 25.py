def check_value_in_list(n):
	list = [1, 5, 3, 8]
	if (n in list):
		return "True"
	else:
		return "False"

print(check_value_in_list(8))
print(check_value_in_list(-1))