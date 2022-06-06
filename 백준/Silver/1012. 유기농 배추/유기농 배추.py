import sys
from collections import deque

t = int(sys.stdin.readline())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
# 반복해야 할 곳
for p in range (t) :
	m, n, k = map(int, sys.stdin.readline().split())
	mp = []
	for i in range (n) :
		mp.append([0 for i in range (m)])

	for i in range (k) :
		x, y = map(int, sys.stdin.readline().split())
		mp[y][x] = 1

	cnt = 2
	def bfs(x1, y1) :
		mp[y1][x1] = cnt
		que = deque()
		que.append((x1, y1))
		while (que) :
			x1, y1 = que.popleft()
			for i in range (4) :
				nx = x1 + dx[i]
				ny = y1 + dy[i]
				if (nx < 0 or ny < 0 or nx >= m or ny >= n) :
					continue
				if (mp[ny][nx] == 0) :
					continue
				if (mp[ny][nx] == 1) :
					mp[ny][nx] = cnt
					que.append((nx, ny))

	for i in range (n) :
		for j in range (m) :
			if (mp[i][j] == 1) :
				bfs(j, i)
				cnt += 1

	print(cnt - 2)