import sys

t = int(sys.stdin.readline())
for i in range (t) :
	n = int(sys.stdin.readline())
	res = 1
	lst = dict()

	for j in range (n) :
		clothes, tag = map(str, sys.stdin.readline().split())
		if (tag not in lst) :
			lst[tag] = [clothes]
		else :
			lst[tag].append(clothes)

	for l in lst :
		res *= (len(lst[l]) + 1)
	res -= 1
	sys.stdout.write(str(res) + '\n')
