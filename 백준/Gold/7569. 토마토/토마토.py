import sys
from collections import deque

m, n, h = map(int, sys.stdin.readline().split())
dx = [0, 0, -1, 1, 0, 0]
dy = [-1, 1, 0, 0, 0, 0]
dh = [0, 0, 0, 0, -1, 1]
lst = []
que = deque()
for i in range (h) :
	tmp = []
	for i in range (n) :
		tmp.append(list(map(int, sys.stdin.readline().split())))
	lst.append(tmp)

def check_tomato(lst) :
	for k in range (h) :
		for i in range (n) :
			for j in range (m) :
				if (lst[k][i][j] == 0) :
					return (0)
	return (1)

def bfs() :
	value = 0
	while (que) :
		x, y, z = que.popleft()
		for i in range (6) :
			nx = x + dx[i]
			ny = y + dy[i]
			nz = z + dh[i]
			if (nx < 0 or ny < 0 or nz < 0 or nx >= m or ny >= n or nz >= h) :
				continue
			if (lst[nz][ny][nx] >= 1) :
				continue
			if (lst[nz][ny][nx] == 0) :
				lst[nz][ny][nx] = lst[z][y][x] + 1
				value = lst[z][y][x] + 1
				que.append((nx, ny, nz))
	return (value)

for k in range (h) :
	for i in range(n) :
		for j in range (m) :
			if (lst[k][i][j] == 1) :
				que.append((j, i, k))

max_value = bfs()
if (check_tomato(lst)) :
	max_value -= 1
	if (max_value == -1) :
		print(0)
	else :
		print(max_value)
else :
	print(-1)