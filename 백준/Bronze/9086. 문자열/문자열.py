import sys

t = int(sys.stdin.readline())
for i in range (t) :
	tmp = sys.stdin.readline().rstrip('\n')
	print(tmp[0]+tmp[-1])
