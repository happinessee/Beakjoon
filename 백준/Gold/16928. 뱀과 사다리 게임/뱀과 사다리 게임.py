import sys
from collections import deque
#사다리, 뱀의 개수
n, m = map(int, sys.stdin.readline().split())
lst = dict()

for i in range (n) :
	x, y = map(int, sys.stdin.readline().split())
	lst[x] = y

for i in range (m) :
	x, y = map(int, sys.stdin.readline().split())
	lst[x] = y

def	bfs(init) :

	def check_cond(curr, cnt) :
		if (curr < 101 and curr not in visited) :
			if (curr in lst) :
				que.append((lst[curr], cnt + 1))
				visited.append(lst[curr])
			else :
				que.append((curr, cnt + 1))
				visited.append(curr)
	
	que = deque([(init, 0)])
	visited = []
	cnt = 0
	while (que) :
		curr, cnt = que.popleft()
		if (curr == 100) :
			return (cnt)
		curr += 1
		check_cond(curr, cnt)
		curr += 1
		check_cond(curr, cnt)
		curr += 1
		check_cond(curr, cnt)
		curr += 1
		check_cond(curr, cnt)
		curr += 1
		check_cond(curr, cnt)
		curr += 1
		check_cond(curr, cnt)

print(bfs(1))
