import sys

# 최대공약수
def gcd(a, b) :
	while (b != 0) :
		r = a % b
		a = b
		b = r
	return (a)

# 최소공배수
def lcm (a, b) :
	return ((a * b) // gcd(a, b))

idx = 0
t = int(sys.stdin.readline())
for i in range (t) :
	m, n, x, y = map(int, sys.stdin.readline().split())
	last = lcm(m, n)
	flag = 1
	for j in range (x, last + 1, m) :
		tmp = n if (j % n) == 0 else j % n
		if (tmp == y) :
			sys.stdout.write(str(j) + '\n')
			flag = 0
			break
	if (flag) :
		sys.stdout.write("-1\n")
