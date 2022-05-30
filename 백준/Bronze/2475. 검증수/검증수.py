import sys

arr = list(map(int, sys.stdin.readline().split()))
tmp = 0

for i in range (len(arr)) :
	tmp += (arr[i] * arr[i])

print(tmp % 10)