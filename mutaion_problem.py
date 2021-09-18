def mutate_string(string, position, character):
    # z=""
    # for iteration, i in enumerate(string):
    #     if iteration == position:
    #         i = character
    #     z+=i

    #Another Solution 
    string = string[:position] + character + string[position+1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

