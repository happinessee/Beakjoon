import sys

t = int(sys.stdin.readline())
idx = 0

sum_lst = [0 for i in range(11)]
sum_lst[0] = 0
sum_lst[1] = 1
sum_lst[2] = 2
sum_lst[3] = 4

for j in range (4, 11) :
	sum_lst[j] = sum_lst[j - 1] + sum_lst[j - 2] + sum_lst[j - 3]

for i in range (t) :
	num = int(sys.stdin.readline())
	print(sum_lst[num])