import sys
from collections import deque

n = int(sys.stdin.readline())
graph = dict()
for i in range (n) :
	rd = list(map(int, sys.stdin.readline().split()))
	for j in range (n) :
		if (rd[j] == 1) :
			if (i not in graph) :
				graph[i] = [j]
			else :
				graph[i].append(j)

lst = [[0 for i in range (n)] for i in range (n)]

def bfs(root, graph) :
	que = deque([root])
	flag = 0
	visited = []
	while (que) :
		n = que.popleft()
		if (n not in visited) :
			if (flag) :
				visited.append(n)
			if (n in graph) :
				flag = 1
				tmp = list(set(graph[n]) - set(visited))
				tmp.sort()
				que += tmp	
	return (visited)

for i in range (n) :
	temp = bfs(i, graph)
	for j in range (n) :
		if (j in temp) :
			lst[i][j] = 1

for i in range (n) :
	print(*lst[i])
