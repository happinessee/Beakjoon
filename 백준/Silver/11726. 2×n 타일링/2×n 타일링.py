import sys

n = int(sys.stdin.readline())
sol = []
for i in range (n + 1) :
	sol.append(0)
if (n == 1) :
	print(1)
	exit(0)
if (n == 2) :
	print(2)
	exit(0)

sol[1] = 1
sol[2] = 2

for i in range (3, n + 1) :
	sol[i] = sol[i - 1] + sol[i - 2]
print(sol[n] % 10007)
