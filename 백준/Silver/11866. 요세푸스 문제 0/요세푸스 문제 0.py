import sys
from collections import deque

def	yosepuse(que, num) :
	for i in range (num) :
		que.append(que.popleft())
	if (len(que) == 1) :
		print(que.popleft(), end = '')
	else :
		print(que.popleft(), end = ', ')
	return (que)

n, k = map(int, sys.stdin.readline().split())

arr = deque()
for i in range (1, n + 1) :
	arr.append(i)

print('<', end = '')
while (len(arr)) :
	yosepuse(arr, k - 1)
print('>', end = '')
