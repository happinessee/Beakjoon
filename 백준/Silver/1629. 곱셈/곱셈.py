import sys
# get  "(a ** b) % c"  value.
a, b, c = map(int, sys.stdin.readline().split())

def dac(a_num, b_num) :
	if (b_num == 1) :
		return (a_num % c)
	tmp = dac(a_num, b_num // 2)

	if (b_num % 2 == 0) :
		return ((tmp * tmp) % c)
	else :
		return ((tmp * tmp * a_num) % c)

print(dac(a, b))