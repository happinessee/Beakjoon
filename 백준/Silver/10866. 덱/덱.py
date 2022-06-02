import sys
from collections import deque

n = int(sys.stdin.readline())
que = deque()

def	push_front(que, num) :
	que.appendleft(num)
	return (que)

def	push_back(que, num) :
	que.append(num)
	return (que)

def front(que) :
	print(que[0])

def	pop_front(que) :
	print(que.popleft())
	return (que)

def	pop_back(que) :
	print(que.pop())
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
	tmp = list(map(str, sys.stdin.readline().split()))
	try : 
		if (tmp[0] == "front") :
			front(que)
		elif (tmp[0] == "pop_front") :
			que = pop_front(que)
		elif (tmp[0] == "pop_back") :
			que = pop_back(que)
		elif (tmp[0] == "empty") :
			empty(que)
		elif (tmp[0] == "size") :
			size(que)
		elif (tmp[0] == "back") :
			back(que)
		elif (tmp[0] == "push_front") :
			que = push_front(que, int(tmp[1]))
		else :
			que = push_back(que, int(tmp[1]))
	except :
		print(-1)