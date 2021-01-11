def calculate(num1,num2,num3):
	sum = num1 + num2 + num3
	if (num1 == num2 and num2 == num3):
		return sum*3
	else:
		return sum

print(calculate(3,3,4))	