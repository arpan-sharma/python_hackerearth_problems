if __name__ == '__main__':
    N = int(input())
    blank_list = []
    for _ in range(N):
    	name, *line = input().split()
    	number = list(map(float, line))



    	if name == 'insert':
    		for iteration, item in enumerate(number):
    			# print(iteration)
    			if iteration == 0:
    				i = int(item)
    			if iteration == 1:
    				z = int(item)

    		blank_list.insert(i,z)


    	elif name == 'remove':
    		for iteration, item in enumerate(number):
    			val = item
    		blank_list.remove(val)

    	elif name == 'append':
    		for iteration, item in enumerate(number):
    			val = item
    		blank_list.append(int(val))

    	elif name == 'sort':
    		blank_list.sort()

    	elif name == 'pop':
    		blank_list.pop()

    	elif name == 'reverse':
    		blank_list.reverse()

    	elif name == 'print':
    		print(blank_list)

    	else:
    		print("Please Select correct input")

		




