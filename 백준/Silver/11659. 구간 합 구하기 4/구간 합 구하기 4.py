import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
s_lst = [0 for _ in range (n + 1)]

for i in range (1, n + 1) :
	s_lst[i] = s_lst[i - 1] + lst[i - 1]

for i in range (m) :
	p1, p2 = map(int, sys.stdin.readline().split())
	sys.stdout.write(str(s_lst[p2] - s_lst[p1 - 1]) + '\n')
