import sys

n, m = map(int, sys.stdin.readline().split())
lan_set = []
for i in range (n) :
	lan_set.append(int(sys.stdin.readline().rstrip('\n')))

length = 1
max_length = max(lan_set)

while (length <= max_length) :
	mid = (length + max_length) // 2 
	lan_cnt = 0
	for i in (lan_set) :
		lan_cnt += i // mid
	if (lan_cnt >= m) :
		length = mid + 1
	else :
		max_length = mid - 1

print(max_length)