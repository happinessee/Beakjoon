import sys

n = int(sys.stdin.readline())
lst = []
for i in range (n) :
	lst.append(list(map(int, sys.stdin.readline().split())))

p_white = 0
p_blue = 0

def	color_sort(tmp) :
	global p_white
	global p_blue
	if (tmp == 0) :
		p_white += 1
	else :
		p_blue += 1

def div4(x, y, size) :
	tmp = lst[y][x]
	if (size == 1) :
		color_sort(tmp)
		return (0)
	
	for i in range (y, y + size) :
		for j in range (x, x + size) :
			if (lst[i][j] != tmp) :
				size = size // 2
				div4(x, y, size)
				div4(x + size, y, size)
				div4(x, y + size, size)
				div4(x + size, y + size, size)
				return (0)
	color_sort(tmp)
	return (0)

div4(0, 0, n)
print(p_white)
print(p_blue)
