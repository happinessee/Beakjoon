import sys

n, m = map(int, sys.stdin.readline().split())
arr0 = []
arr1 = []
for i in range (n) :
	arr0.append(list(map(int, sys.stdin.readline().split())))
for j in range (n) :
	arr1.append(list(map(int, sys.stdin.readline().split())))

res = []
for i in range (n) :
	tmp = []
	for j in range (m) :
		tmp.append(arr0[i][j] + arr1[i][j])
	res.append(tmp)

for i in range (n) :
	print(*res[i])