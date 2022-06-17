import sys

INF = 200
n, m = map(int, sys.stdin.readline().split())
res = [[INF] * n for i in range (n)]
for i in range (n) :
		res[i][i] = 0

for i in range (m) :
	x, y = map(int, sys.stdin.readline().split())
	res[y - 1][x - 1] = 1
	res[x - 1][y - 1] = 1

def floyd_warshall() :
	dist = [[INF] * n for i in range (n)]
	for i in range (n) :
		for j in range (n) :
			dist[i][j] = res[i][j]
	
	for i in range (n) :
		for j in range (n) :
			for k in range (n) :
				if (dist[j][k] > dist[j][i] + dist[i][k]) :
					dist[j][k] = dist[j][i] + dist[i][k]
	return (dist)

lst = [sum(l) for l in floyd_warshall()]
print(lst.index(min(lst)) + 1)
