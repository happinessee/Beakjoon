import sys
from collections import deque

def d(n) :
	n = 2 * n if 2 * n < 10000 else (2 * n) % 10000
	return (n)

def s(n) :
	n = n - 1 if n != 0 else 9999
	return (n)

def l(n) :
	tmp = n % 1000
	tmp2 = n // 1000
	n = tmp * 10 + tmp2
	return (n)

def r(n) :
	tmp = n % 10
	tmp2 = n // 10
	n = tmp * 1000 + tmp2
	return (n)

def bfs(num_init, visit) :
	que = deque([(num_init, visit)])
	visited[num_init] = 0
	while (que) :
		current_num, visit = que.popleft()
		if (current_num == n) :
			return (visit)
		tp = d(current_num)
		if (visited[tp]) :
			que.append((tp, visit + "D"))
			visited[tp] = 0
		tp = s(current_num)
		if (visited[tp]) :
			que.append((tp, visit + "S"))
			visited[tp] = 0
		tp = l(current_num)
		if (visited[tp]) :
			que.append((tp, visit + "L"))
			visited[tp] = 0
		tp = r(current_num)
		if (visited[tp]) :
			que.append((tp, visit + "R"))
			visited[tp] = 0

t = int(sys.stdin.readline())
for i in range (t) :
	visited = [1 for _ in range (10001)]
	cur_num, n = map(int, sys.stdin.readline().split())
	sys.stdout.write(str(bfs(cur_num, "")) + '\n')
