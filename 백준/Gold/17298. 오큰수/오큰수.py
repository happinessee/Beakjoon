from collections import deque
import sys

n = int(sys.stdin.readline())
que = list(map(int, sys.stdin.readline().split()))
res = [-1 for i in range (n)]
s = list()

for i in range (n) :
	while (s and que[s[-1]] < que[i]) :
		res[s.pop()] = que[i]
	s.append(i)

print(*res)
