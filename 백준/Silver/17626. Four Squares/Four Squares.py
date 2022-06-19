import sys

n = int(sys.stdin.readline())
lst = set()
lst2 = set()
lst3 = set()

for i in range (1, int(n ** (1/2)) + 1) :
	lst.add(i ** 2)

if (n in lst) :
	print(1)
	exit()

tmp = [_ for _ in lst]
for i in (lst) :
	for j in (tmp) :
		lst2.add(i + j)

if (n in lst2) :
	print(2)
	exit()

for i in (lst2) :
	for j in (tmp) :
		lst3.add(i + j)

if (n in lst3) :
	print(3)
	exit()

else :
	print(4)
