import sys

n = int(sys.stdin.readline())
lst = []
for i in range (n) :
	lst.append(list(map(int, sys.stdin.readline().rstrip('\n'))))

def quad_tree(x_start, y_start, t) :
	tmp = lst[y_start][x_start]
	if (t == 1) :
		print(tmp, end = '')
		return (0)
	for i in range (y_start, t + y_start) :
		for j in range (x_start, t + x_start) :
			if (lst[i][j] != tmp) :
				print('(', end = '')
				quad_tree(x_start, y_start, t // 2)
				quad_tree(x_start + (t // 2), y_start, t // 2)
				quad_tree(x_start, y_start + (t // 2), t // 2)
				quad_tree(x_start + (t // 2), y_start + (t // 2), t // 2)
				print(')', end = '')
				return (0)
	print(tmp, end = '')
	return (0)

quad_tree(0, 0, n)
