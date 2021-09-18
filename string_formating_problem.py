def print_formatted(number):
	for i in range(1,number+1):
		print(f'{i}'+' '+f'{oct(i)[2:]}'+' '+f'{hex(i)[2:].upper()}'+' '+f'{bin(i)[2:]}'+' ')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)