import sys

t, target = map(int, sys.stdin.readline().split())
lst = []
for i in range (t) :
	lst.append(int(sys.stdin.readline()))
lst.sort(reverse=True)

now = 0
cnt = 0
while (1) :
	for i in lst :
		if (now + i <= target) :
			cnt += 1
			now += i
			break
	if (target-now == 0) :
		print(cnt)
		exit(0)