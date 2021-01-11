def check_vowel(c):
	c = input("Please input a letter:\n")
	vowel = ["u","e","o","a","i"]
	if (c in vowel):
		return c + " is a vowel"
	else:
		return c + " is not a vowel"

print(check_vowel("a"))