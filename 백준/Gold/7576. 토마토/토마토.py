import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
m, n = map(int, sys.stdin.readline().split())
lst = []
que = deque()
for i in range (n) :
	lst.append(list(map(int, sys.stdin.readline().split())))

def check_tomato(lst) :
	for i in range (n) :
		for j in range (m) :
			if (lst[i][j] == 0) :
				return (0)
	return (1)

def bfs() :
	while (que) :
		x, y = que.popleft()
		for i in range (4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if (nx < 0 or ny < 0 or nx >= m or ny >= n) :
				continue
			if (lst[ny][nx] >= 1) :
				continue
			if (lst[ny][nx] == 0) :
				lst[ny][nx] = lst[y][x] + 1
				que.append((nx, ny))

for i in range(n) :
	for j in range (m) :
		if (lst[i][j] == 1) :
			que.append((j, i))
bfs()

if (check_tomato(lst)) :
	t = max(map(max, lst)) - 1
	if (t == -2) :
		print(0)
	else :
		print(t)
else :
	print(-1)
