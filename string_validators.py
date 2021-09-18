if __name__ == '__main__':
    s = input()
    c = False
    d = False
    e = False
    f = False
    g = False

    for i in s:
    	x = i.isalnum()
    	y = i.isalpha()
    	z = i.isdigit()
    	a = i.islower()
    	b = i.isupper()

    	if x == True:
    		c = True

    	if y == True:
    		d = True

    	if z == True:
    		e = True

    	if a == True:
    		f = True

    	if b == True:
    		g = True
    print(c)
    print(d)
    print(e)
    print(f)
    print(g)

