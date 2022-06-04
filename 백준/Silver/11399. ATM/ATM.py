import sys

n = int(sys.stdin.readline())

lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

tmp = 0
for i in range(len(lst) - 1) :
	lst[i + 1] = lst[i] + lst[i + 1]

print(sum(lst))
