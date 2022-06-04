import sys

t = int(sys.stdin.readline())
fibo_set = [[1, 0], [0, 1], [1, 1]]
for i in range (38) :
	fibo_set.append([0, 0])

def fibo(n) :
	if (n == 0) :
		return (fibo_set[0])
	if (n == 1) :
		return (fibo_set[1])
	if (n == 2) :
		return (fibo_set[2])
	if (fibo_set[n] != [0, 0]) :
		return (fibo_set[n])
	else :
		fibo_set[n] = [x+y for x, y in zip(fibo(n - 1), fibo(n - 2))]
		return (fibo(n))

fibo(40)
for i in range (t) :
	n = int(sys.stdin.readline())
	print(*fibo_set[n])
