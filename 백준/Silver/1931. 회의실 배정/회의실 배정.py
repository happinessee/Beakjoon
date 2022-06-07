import sys

t = int(sys.stdin.readline())
lst = []
for i in range (t) :
	st, end = map(int, sys.stdin.readline().split())
	lst.append([st, end])
lst.sort()
lst.sort(key = lambda x : x[1])

cnt, n = 0, 0
for st, end in lst :
	if (st >= n) :
		n = end
		cnt += 1

print(cnt)
