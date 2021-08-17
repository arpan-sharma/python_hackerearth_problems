if __name__ == '__main__':
    name_score = []
    for_min = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        name_score.append([name,score])
        for_min.append(score)

for_min_score = min(for_min)
for_min.remove(for_min_score)

for i in for_min:
	
	if for_min_score == i:
		for_min.remove(i)
if for_min_score in for_min:
	for_min.remove(for_min_score)

for_min_score = min(for_min)

name_score = sorted(name_score)


for x in name_score:
	if x[1] == for_min_score:
		print(x[0])

