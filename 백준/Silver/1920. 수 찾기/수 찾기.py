import sys

n = int(sys.stdin.readline())
n_set = dict(dict.fromkeys(list(map(int, sys.stdin.readline().split())), 1))

m = int(sys.stdin.readline())
m_set = list(map(int, sys.stdin.readline().split()))

for i in range (m) :
	if (m_set[i] in n_set) :
		print(1)
	else :
		print(0)