import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
dx = [-1, 1]
graph = []
for i in range (100001) :
	graph.append(0)
graph[n] = 1
def bfs(x) :
	que = deque()
	que.append(x)
	while (que) :
		x = que.popleft()
		for i in range (3) :
			if (i < 2) :
				nx = x + dx[i]
			else :
				nx = x * 2
			if (nx > 100000 or nx < 0) :
				continue
			if (graph[nx] == 0) :
				graph[nx] = graph[x] + 1
				que.append(nx)
			if (nx == k) :
				print(graph[nx] - 1)
				exit(0)
bfs(n)