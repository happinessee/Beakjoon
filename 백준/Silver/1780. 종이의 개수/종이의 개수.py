import sys

n = int(sys.stdin.readline())
lst = list()
for i in range (n) :
	lst.append(list(map(int, sys.stdin.readline().split())))

ans_1 = 0
ans0 = 0
ans1 = 0

def dec(tmp) :
	global ans_1
	global ans0
	global ans1

	if (tmp == -1) :
		ans_1 += 1
	elif (tmp == 0) :
		ans0 += 1
	else :
		ans1 += 1
	return (0)

def rec3(x, y, size) :
	tmp = lst[y][x]

	if (size == 1) :
		dec(tmp)
		return (0)

	for i in range (y, y + size) :
		for j in range (x, x + size) :
			if (tmp != lst[i][j]) :
				size = size // 3
				rec3(x, y, size)
				rec3(x, y + size, size)
				rec3(x, y + 2 * size, size)
				rec3(x + size, y, size)
				rec3(x + size * 2, y, size)
				rec3(x + size, y + size, size)
				rec3(x + size * 2, y + size, size)
				rec3(x + size, y + size * 2, size)
				rec3(x + size * 2, y + size * 2, size)
				return (0)
	dec(tmp)
	return (0)

rec3(0, 0, n)
print(ans_1, ans0, ans1)