import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
remote = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if (m != 0) :
	remove = list(map(int, sys.stdin.readline().split()))
if (m != 0) :
	remote = list(set(remote) - set(remove))
min_cnt = abs(100 - n)

for i in range (1000001) :
	i = str(i)

	for j in range (len(i)) :
		if (int(i[j]) not in remote) :
			break
		elif (j == len(i) - 1) :
			min_cnt = min(min_cnt, abs(int(i) - n) + len(i))

print(min_cnt)