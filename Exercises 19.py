def new_string(str):
	if (str.startswith("Is")):
		return str
	else:
		return "Is " + str

print(new_string("Isjava"))
print(new_string("java"))