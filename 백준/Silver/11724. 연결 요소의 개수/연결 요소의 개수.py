import sys
from collections import deque

# 정점의 개수, 간선의 개수
n, m = map(int, sys.stdin.readline().split())
graph = {}

def	bfs(graph, root) :
	visited = []
	que = deque([root])

	while (que) :
		n = que.popleft()
		if (n not in visited) :
			visited.append(n)
			if (n in graph) :
				tmp = list(set(graph[n]) - set(visited))
				tmp.sort()
				que += tmp
	return (visited)

for i in range (1, n + 1) :
	graph[i] = [100000 + i]

for i in range (m) :
	u, v = map(int, sys.stdin.readline().split())
	if (u not in graph) :
		graph[u].append(v)
	elif (v not in graph[u]) :
		graph[u].append(v)
	if (v not in graph) :
		graph[v].append(u)
	elif (u not in graph[v]) :
		graph[v].append(u)

cnt = 0
visited = []
for (key, value) in graph.items() :
	if (key not in visited) :
		visited += bfs(graph, key)
		cnt += 1

print(cnt)