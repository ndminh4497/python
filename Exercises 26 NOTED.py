def histogram(items):
	for n in items:
		output = ''
		times = n
		while (times > 0):
			output += '*' #output = output + '*'
			times = times - 1 #times -= 1
		print(output)
		
histogram([10,10-1,10-2,(10-3)+5])