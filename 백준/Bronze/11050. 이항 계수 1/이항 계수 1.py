import sys

n, k = map(int, sys.stdin.readline().split())

tmp = 1
for i in range (2, n + 1) :
	tmp *= i

tmp2 = 1
for i in range (2, k + 1) :
	tmp2 *= i
for i in range (2, n - k + 1) :
	tmp2 *= i

print (tmp // tmp2)