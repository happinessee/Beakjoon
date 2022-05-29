import sys

n = int(sys.stdin.readline())
num_set_init = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
check_set = list(map(int, sys.stdin.readline().split()))

num_dict = dict()

for i in num_set_init :
	if (i not in num_dict) :
		num_dict[i] = 1
	else :
		num_dict[i] += 1

for i in range(m - 1) :
	print(num_dict.get(check_set[i], '0'), end = ' ')
print(num_dict.get(check_set[m - 1], '0'), end = '')