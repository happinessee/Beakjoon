import sys

lst = list(map(int, sys.stdin.readline().rstrip('\n')))
tmp = 0
for i in lst :
	tmp += (i ** 5)
print(tmp)