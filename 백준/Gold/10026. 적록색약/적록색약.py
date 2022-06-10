import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n = int(sys.stdin.readline())
graph = []
for i in range (n) :
	graph.append(list(map(str, sys.stdin.readline().rstrip('\n'))))

graph2 = []
for i in graph :
	tmp = []
	for j in i :
		if (j == 'G') :
			tmp.append('R')
		else :
			tmp.append(j)
	graph2.append(tmp)

def bfs(x, y, color, cnt) :
	que = deque()
	que.append((x, y))
	while (que) :
		x, y = que.popleft()
		for i in range (4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if (nx < 0 or ny < 0 or nx >= n or ny >= n) :
				continue
			if (graph[ny][nx] == color) :
				que.append((nx, ny))
				graph[ny][nx] = str(cnt)

def bfs2(x, y, color, cnt) :
	que = deque()
	que.append((x, y))
	while (que) :
		x, y = que.popleft()
		for i in range (4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if (nx < 0 or ny < 0 or nx >= n or ny >= n) :
				continue
			if (graph2[ny][nx] == color) :
				que.append((nx, ny))
				graph2[ny][nx] = str(cnt)

colors = ['R', 'G', 'B']
cnt = 0
cnt2 = 0
for i in range (n) :
	for j in range (n) :
		if (graph[i][j] in colors) :
			bfs(j, i, graph[i][j], cnt)
			cnt += 1
		if (graph2[i][j] in colors) :
			bfs2(j, i, graph2[i][j], cnt2)
			cnt2 += 1

print(cnt, cnt2)
