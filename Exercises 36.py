#Solution 1
def check_int(a,b):
	if (isinstance(a,int) and isinstance(b,int)):
		return a + b
	else:
		return ("Input must be Integer")

print(check_int(6,5))

# Solution 2
# def check_int2(a,b):
# 	if not (isinstance(a,int) and isinstance(b,int)):
# 		raise TypeError("Input must be Integer")
# 	return a + b	

# print(check_int2(6.5,5))