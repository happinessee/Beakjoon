import sys

n = int(sys.stdin.readline())
lst = []
for i in range (n) :
	lst.append(list(map(int, sys.stdin.readline().split())))

if (n == 1) :
	print(lst[0][0])
	exit(0)

res = lst[0][0]

for i in range (1, n) :
	for j in range (0, i + 1) :
		if (j == 0) :
			lst[i][j] += lst[i - 1][j]
		elif (j == i) :
			lst[i][j] += lst[i - 1][j - 1]
		else :
			lst[i][j] += max(lst[i - 1][j - 1], lst[i - 1][j])
		res = max(lst[i][j], res)

print(res)
