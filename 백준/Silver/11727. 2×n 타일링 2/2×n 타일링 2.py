import sys

n = int(sys.stdin.readline())
lst = []
lst.append(0)
lst.append(1)
lst.append(3)
for i in range (3, 1002) :
	lst.append(lst[i - 1] + 2 * lst[i - 2])

print(lst[n] % 10007)