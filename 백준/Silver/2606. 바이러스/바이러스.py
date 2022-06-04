import sys

def DFS(graph, root) :
	visited = []
	stack = [root]

	while (stack) :
		n = stack.pop()
		if (n not in visited) :
			visited.append(n)
			if (n in graph) :
				tmp = list(set(graph[n]) - set(visited))
				tmp.sort(reverse=True)
				stack += tmp
	return visited

graph = {}
node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

for i in range (edge) :
	n1, n2 = map(int, sys.stdin.readline().split())
	if (n1 not in graph) :
		graph[n1] = [n2]
	elif (n2 not in graph[n1]) : 
		graph[n1].append(n2)
	if (n2 not in graph) :
		graph[n2] = [n1]
	elif (n1 not in graph[n2]) :
		graph[n2].append(n1)

visited = DFS(graph, 1)
print(len(visited) - 1)