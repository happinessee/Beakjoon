import sys

n, m = map(int, sys.stdin.readline().split())
lst = list()
for i in range (n) :
	lst.append(list(map(int, sys.stdin.readline().split())))

def tet1(x, y) :
	try :
		return (lst[y][x] + lst[y][x + 1] + lst[y][x + 2] + lst[y][x + 3])
	except :
		return (0)

def tet2(x, y) :
	try :
		return (lst[y][x] + lst[y + 1][x] + lst[y + 2][x] + lst[y + 3][x])
	except :
		return (0)

def tet3(x, y) :
	try :
		return (lst[y][x] + lst[y][x + 1] + lst[y + 1][x] + lst[y + 1][x + 1])
	except :
		return (0)

def tet4(x, y) :
	try :
		return (lst[y][x] + lst[y][x + 1] + lst[y][x + 2] + lst[y + 1][x + 2])
	except :
		return (0)

def tet5(x, y) :
	try :
		return (lst[y][x] + lst[y][x + 1] + lst[y][x + 2] + lst[y + 1][x])
	except :
		return (0)

def tet6(x, y) :
	try :
		return (lst[y][x] + lst[y + 1][x] + lst[y + 2][x] + lst[y + 2][x + 1])
	except :
		return (0)

def tet7(x, y) :
	try :
		return (lst[y + 2][x] + lst[y + 2][x + 1] + lst[y][x + 1] + lst[y + 1][x + 1])
	except :
		return (0)

def tet8(x, y) :
	try :
		return (lst[y][x] + lst[y][x + 1] + lst[y + 1][x + 1] + lst[y + 1][x + 2])
	except :
		return (0)

def tet9(x, y) :
	try :
		return (lst[y + 1][x] + lst[y + 1][x + 1] + lst[y][x + 1] + lst[y][x + 2])
	except :
		return (0)

def tet10(x, y) :
	try :
		return (lst[y][x + 1] + lst[y + 1][x + 1] + lst[y + 1][x] + lst[y + 2][x])
	except :
		return (0)

def tet11(x, y) :
	try :
		return (lst[y][x] + lst[y + 1][x] + lst[y + 1][x + 1] + lst[y + 2][x + 1])
	except :
		return (0)

def tet12(x, y) :
	try :
		return (lst[y][x + 1] + lst[y + 1][x] + lst[y + 1][x + 1] + lst[y + 1][x + 2])
	except :
		return (0)

def tet13(x, y) :
	try :
		return (lst[y][x] + lst[y][x + 1] + lst[y][x + 2] + lst[y + 1][x + 1])
	except :
		return (0)

def tet14(x, y) :
	try :
		return (lst[y + 1][x] + lst[y][x + 1] + lst[y + 1][x + 1] + lst[y + 2][x + 1])
	except :
		return (0)

def tet15(x, y) :
	try :
		return (lst[y][x] + lst[y + 1][x] + lst[y + 2][x] + lst[y + 1][x + 1])
	except :
		return (0)

def tet16(x, y) :
	try :
		return (lst[y][x] + lst[y][x + 1] + lst[y + 1][x + 1] + lst[y + 2][x + 1])
	except :
		return (0)

def tet17(x, y) :
	try :
		return (lst[y][x] + lst[y][x + 1] + lst[y + 1][x] + lst[y + 2][x])
	except :
		return (0)

def tet18(x, y) :
	try :
		return (lst[y][x + 2] + lst[y + 1][x + 2] + lst[y + 1][x + 1] + lst[y + 1][x])
	except :
		return (0)

def tet19(x, y) :
	try :
		return (lst[y][x] + lst[y + 1][x] + lst[y + 1][x + 1] + lst[y + 1][x + 2])
	except :
		return (0)


def mx(x, y, res) :
	return (max(res, tet1(x, y), tet2(x, y), tet3(x, y), tet4(x, y), tet5(x, y) \
			, tet6(x, y), tet7(x, y), tet8(x, y), tet9(x, y), tet10(x, y) \
			, tet11(x, y), tet12(x, y), tet13(x, y), tet14(x, y), tet15(x, y) \
			, tet16(x, y), tet17(x, y), tet18(x, y), tet19(x, y)))

res = 0
for i in range (n) :
	for j in range (m) :
		res = mx(j, i, res)

print(res)