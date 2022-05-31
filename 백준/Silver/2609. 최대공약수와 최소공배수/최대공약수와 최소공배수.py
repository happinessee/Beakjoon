import sys

def	gcd(n, m) :
	if (n % m == 0) :
		return (m)
	else :
		return (gcd(m, n % m))

n, m = map(int, sys.stdin.readline().split())
least_num = gcd(n, m)
print(least_num)
print((n * m) // least_num)
