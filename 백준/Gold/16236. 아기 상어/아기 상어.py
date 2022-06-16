import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
shark = 2
fish = 0
res = 0
lst = list()
n = int(sys.stdin.readline())
for i in range (n) :
	lst.append(list(map(int, sys.stdin.readline().split())))

for i in range (n) :
	for j in range (n) :
		if (lst[i][j] == 9) :
			x_idx = j
			y_idx = i
			break
lst[y_idx][x_idx] = 0

def bfs(x, y) :
	min_dist = 1000
	dist_list = []
	visited = [[0]*n for _ in range(n)]
	visited[y][x] = 1
	que = deque()
	que.append((x, y, 0))
	while (que) :
		x, y, dist = que.popleft()
		for i in range (4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if (nx < 0 or ny < 0 or nx >= n or ny >= n or visited[ny][nx]) :
				continue
			# 움직일 수 있는 칸의 경우
			if (lst[ny][nx] <= shark) :
				visited[ny][nx] = 1
				# 물고기가 있는 경우
				if (0 < lst[ny][nx] < shark) :
					min_dist = dist
					dist_list.append((dist + 1, ny, nx))
				# 물고기 못 먹은 경우
				if (dist + 1 <= min_dist) :
					que.append((nx, ny, dist + 1))
	if dist_list :
		dist_list.sort()
		return (dist_list[0])
	return (0)

def shark_sizeup() :
	global fish
	global shark
	if (fish == shark) :
		fish = 0
		shark += 1

while (1) :
	tmp = bfs(x_idx, y_idx)
	if (not tmp) :
		break
	x_idx, y_idx = tmp[2], tmp[1]
	res += tmp[0]
	fish += 1
	shark_sizeup()
	lst[y_idx][x_idx] = 0

print(res)
