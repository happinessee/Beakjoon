import sys

lst = []
for i in range (28) :
	lst.append(int(sys.stdin.readline()))

res = [i for i in range (1, 31) if i not in lst]
res.sort()
for i in range (2) :
	print(res[i])