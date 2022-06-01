import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque()

def	push(que, num) :
	que.append(num)
	return (que)

def front(que) :
	print(que[0])

def	pop(que) :
	print(que.popleft())
	return (que)

def	empty(que) :
	if (len(que) == 0) :
		print(1)
	else :
		print(0)

def	size(que) :
	print(len(que))

def	back(que) :
	print(que[len(que) - 1])

for i in range (n) :
	tmp = sys.stdin.readline().rstrip('\n')
	try : 
		if (tmp == "front") :
			front(que)
		elif (tmp == "pop") :
			que = pop(que)
		elif (tmp == "empty") :
			empty(que)
		elif (tmp == "size") :
			size(que)
		elif (tmp == "back") :
			back(que)
		else :
			que = push(que, int(tmp[5 : len(tmp)]))
	except :
		print(-1)