import sys

r = 31
m = 1234567891

n = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip('\n')

num_list = []
for i in s :
	num_list.append(ord(i) - 96)

value = 0
for i in range (n) :
	value += num_list[i] * (r ** i)

print(value % m)