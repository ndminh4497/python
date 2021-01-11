def test_number5(a,b):
	if (a == b or a + b == 5 or a - b == 5):
		return True
	else:
		return False

print(test_number5(6, 2))
print(test_number5(3, 2))
print(test_number5(2, 2))