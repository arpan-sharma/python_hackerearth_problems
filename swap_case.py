def swap_case(s):
	z = " "
	for i in s:
		if i.isupper():
			i = i.lower()
			z+= i
		else:
			i = i.upper()
			z+= i
	return z

if __name__ == '__main__':
	val = input()
	print(swap_case(val))
