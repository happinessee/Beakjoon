import sys

n = int(sys.stdin.readline())

def recurs(n, a_list, idx) :
	if (min(a_list) <= idx) :
		return (0)
	if (n == 1) :
		a_list.append(idx)
		return (0)
	if (n % 3 == 0):
		recurs(n // 3, a_list, idx + 1)
	if (n % 2 == 0) :
		recurs(n // 2, a_list,  idx + 1)
	recurs(n - 1, a_list, idx + 1)

if (n == 1) :
	print (0)
	exit(0)

if (n == 2 or n == 3) :
	print (1)
	exit(0)

a_list = [99999999]
recurs(n, a_list, 0)
print(min(a_list))
