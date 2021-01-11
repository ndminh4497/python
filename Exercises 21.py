def check_number(n):
	# n = int(input("Please enter an integer number:\n"))
	if (n % 2 == 0):
		return str(n) +" Is an even number"
	else:
		return str(n) +" Is an odd number"

n = int(input("Please enter an integer number:\n"))
print(check_number(n))			