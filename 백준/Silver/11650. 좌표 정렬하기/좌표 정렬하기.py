import sys

n = int(sys.stdin.readline())

originList = []
for i in range(n) :
	originList.append(list(map(int, sys.stdin.readline().split())))

originList.sort(key=lambda x: x[1])
originList.sort(key=lambda x: x[0])

for i in range(n) :
	sys.stdout.write(str(originList[i][0]))
	sys.stdout.write(' ')
	sys.stdout.write(str(originList[i][1]))
	sys.stdout.write('\n')