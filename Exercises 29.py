color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

# Solution 1
for n in color_list_1:
	if n in color_list_2:
		continue
	if n not in color_list_2:
		print (n)

# Solution 2		
print (color_list_1.difference(color_list_2))		