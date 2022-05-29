import sys

n, m = map(int, sys.stdin.readline().split())

name_set = dict()
cnt = 0

for i in range(n + m) :
	tmp = sys.stdin.readline().rstrip('\n')
	if (tmp not in name_set) :
		name_set[tmp] = 1
	else :
		name_set[tmp] += 1
		cnt += 1

print(cnt)
name_set = sorted(name_set.items())

for key, value in name_set :
	if (value == 2) :
		print(key)