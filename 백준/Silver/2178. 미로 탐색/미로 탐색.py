import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, sys.stdin.readline().split())
graph = []
for i in range (n) :
	graph.append(list(map(int, sys.stdin.readline().rstrip('\n'))))

def BFS(x, y) :
	que = deque()
	que.append((x, y))

	while (que) :
		x, y = que.popleft()
		
		for i in range (4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if (nx < 0 or ny < 0 or nx >= n or ny >= m) :
				continue
			if (graph[nx][ny] == 0) :
				continue
			if (graph[nx][ny] == 1) :
				graph[nx][ny] = graph[x][y] + 1
				que.append((nx, ny))
	return (graph[n - 1][m - 1])

print(BFS(0, 0))
