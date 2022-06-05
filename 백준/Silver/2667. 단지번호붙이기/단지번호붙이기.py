import sys
from collections import deque

n = int(sys.stdin.readline())
lst = []
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for i in range (n) :
	lst.append(list(map(int, sys.stdin.readline().rstrip('\n'))))

house = []
cnt = 2

def	bfs(x, y, cnt) :
	idx = 0
	que = deque()
	que.append((x, y))

	while (que) :
		x, y = que.popleft()

		for i in range (4) :
			nx = x + dx[i]
			ny = y + dy[i]
			if (nx < 0 or ny < 0 or nx >= n or ny >= n) :
				continue
			if (lst[nx][ny] == 0) :
				continue
			if (lst[nx][ny] == 1) :
				lst[nx][ny] = cnt
				que.append((nx, ny))
				idx += 1
	return (idx)

g_flag = 1
while (g_flag) :
	flag = 0
	for i in range (n) :
		for j in range (n) :
			if (lst[i][j] == 1) :
				tmp = bfs(i, j, cnt)
				if (tmp == 0) :
					house.append(1)
				else :
					house.append(tmp)
				cnt += 1
			if (i == (n - 1) and j == (n - 1)) :
				g_flag = 0

print(cnt - 2)
house.sort()
for i in house :
	print(i)
