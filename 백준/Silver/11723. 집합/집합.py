import sys

m = int(sys.stdin.readline())
s = set()

def add(x) :
	s.add(x)

def remove(x) :
	try :
		s.remove(x)
	except :
		return (1)

def check(x) :
	if (x in s) :
		sys.stdout.write(str(1) + '\n')
	else :
		sys.stdout.write(str(0) + '\n')

def toggle(x) :
	if (x in s) :
		remove(x)
	else :
		add(x)

def	all() :
	s = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
	return (s)

def	empty() :
	s = set()
	return (s)

for i in range (m) :
	comm = list(map(str, sys.stdin.readline().rstrip().split()))
	if (comm[0] == 'add') :
		add(int(comm[1]))
	elif (comm[0] == 'remove') :
		remove(int(comm[1]))
	elif (comm[0] == 'check') :
		check(int(comm[1]))
	elif (comm[0] == 'toggle') :
		toggle(int(comm[1]))
	elif (comm[0] == 'all') :
		s = all()
	else :
		s = empty()
