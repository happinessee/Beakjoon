import sys
from collections import deque

def DFS(graph, root) :
	visited = []
	stack = [root]

	while (stack) :
		n = stack.pop()
		if (n not in visited) :
			visited.append(n)
			if (n in graph) :
				tmp = list(set(graph[n]) - set(visited))
				tmp.sort(reverse = True)
				stack += tmp
	return " ".join(str(i) for i in visited)

def	BFS(graph, root) :
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
	return " ".join(str(i) for i in visited)

graph = {}
node, edge, start = map(int, (sys.stdin.readline().split()))

for i in range (edge) :
	n1, n2 = map(int, (sys.stdin.readline().split()))
	if (n1 not in graph) :
		graph[n1] = [n2]
	elif (n2 not in graph[n1]) :
		graph[n1].append(n2)
	
	if (n2 not in graph) :
		graph[n2] = [n1]
	elif (n1 not in graph[n2]) :
		graph[n2].append(n1)

print(DFS(graph, start))
print(BFS(graph, start))
