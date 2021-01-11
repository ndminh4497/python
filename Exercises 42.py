def concatenation_str(mystr):
	if(len(mystr) >= 2):
		newstr = mystr[:2] + mystr[-2:]
	else:
		newstr = 'Empty String'
	return newstr

print(concatenation_str('w3resource'))
print(concatenation_str('w3'))
print(concatenation_str('w'))


			