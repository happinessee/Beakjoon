import sys
from collections import deque

def	act_que(num_list) :
	num_list.append(num_list.popleft())
	return (num_list)

n = int(sys.stdin.readline())
num_set = deque()

for i in range (n) :
	num_set.append(i + 1)

while (len(num_set) != 1) :
	num_set.popleft()
	num_set = act_que(num_set)

print (num_set[0])
