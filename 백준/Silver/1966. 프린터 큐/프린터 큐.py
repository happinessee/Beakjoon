import sys
from collections import deque

def	print_que(num_list) :
	num_list.append(num_list.popleft())
	return (num_list)

n = int(sys.stdin.readline())

for i in range (n) :
	num, check_num = map(int, (sys.stdin.readline().split()))
	num_list = deque(map(int, sys.stdin.readline().split()))
	cnt = 0
	while (len(num_list)) :
		if (num_list[0] == max(num_list)) :
			cnt += 1
			num_list.popleft()
			if (check_num == 0) :
				print(cnt)
				break
			else :
				check_num -= 1
		else :
			num_list = print_que(num_list)
			if (check_num == 0) :
				check_num = len(num_list) - 1
			else :
				check_num -= 1
