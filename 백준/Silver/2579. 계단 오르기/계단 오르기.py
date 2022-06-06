import sys

n = int(sys.stdin.readline())
if (n == 0) :
	print(0)
	exit(0)

lst = []
for i in range (n) :
	lst.append(int(sys.stdin.readline()))

if (n == 1) :
	print(lst[0])
	exit(0)
if (n == 2) :
	print(lst[0] + lst[1])
	exit(0)

res = []
res.append(lst[0])
res.append(lst[0] + lst[1])
res.append(max((lst[0] + lst[2]), (lst[1] + lst[2])))

for i in range (3, n) :
	res.append(max((res[i - 2] + lst[i]), (res[i - 3] + lst[i - 1] + lst[i])))

print(res[n - 1])
