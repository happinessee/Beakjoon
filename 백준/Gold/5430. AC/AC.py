import sys
from collections import deque

t = int(sys.stdin.readline())

for i in range (t) :
	rev = 0
	func = sys.stdin.readline().rstrip('\n')
	n = int(sys.stdin.readline())
	lst = list(sys.stdin.readline().strip('[]\n').split(','))
	lst = deque([i for i in lst if i != ''])
	try :
		for k in func :
			if k == 'R' :
				if (rev == 0) :
					rev = 1
				else :
					rev = 0
			else :
				if (rev == 1) :
					lst.pop()
				else :
					lst.popleft()
	except :
		sys.stdout.write('error\n')
		continue
	if (rev == 1) :
		lst.reverse()
	sys.stdout.write('[')
	sys.stdout.write(",".join(list(lst)))
	sys.stdout.write(']\n')
