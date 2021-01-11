def mix_up(a,b):

	newstring = a[:2] + b[-1:]
	newstring2 = b[:2] + a[-1:]
	newstring3 = newstring + ' ' + newstring2
	return newstring3

print(mix_up('abc','xyz'))	

