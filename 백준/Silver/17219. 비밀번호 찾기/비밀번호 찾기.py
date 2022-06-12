import sys

n, m = map(int, sys.stdin.readline().split())
lst = dict()

for i in range (n) :
	site, pwd = map(str, sys.stdin.readline().split())
	lst[site] = pwd

for i in range (m) :
	site = sys.stdin.readline().rstrip('\n')
	sys.stdout.write(lst[site] + '\n')