def copy_string(str):
	
	if (len(str) <= 2):
		return str*n
	else:
		return str[:2]

str = 'Ng'
n = int(input("Please input an integer number:\n"))
print(copy_string(str))

