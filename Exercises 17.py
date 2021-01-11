def near_thousand(number):
	return ((abs(1000-number) <= 100) or (abs(2000-number) <= 100))
print(near_thousand(1000))
print(near_thousand(100))

