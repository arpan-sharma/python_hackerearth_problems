if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    values = student_marks[query_name]
    i = 0.00
    z = 0.00
    for x in values:
    	z+=1
    	i+=x
    format_float = "{:.2f}".format(i/z)
    print(format_float)