import sys

n = int(sys.stdin.readline())

cnt, sum = 0,0
for i in range(1, n+1) :
    sum += i
    if (n - sum >= 0 and (n - sum) % i == 0):
        cnt += 1
    if (n < sum):
        break

sys.stdout.write(str(cnt))
