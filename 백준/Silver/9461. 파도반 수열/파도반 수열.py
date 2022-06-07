import sys

t = int(sys.stdin.readline())
lst = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16]
for i in range (11, 101) :
	lst.append(lst[i] + lst[i - 4])

for i in range (t) :
	print(lst[int(sys.stdin.readline()) - 1])