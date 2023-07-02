import sys

n, m = map(int, sys.stdin.readline().split())
    
array = []
for i in range(n) :
    array.append(list(map(int, sys.stdin.readline().split())))

# 누적합 배열을 생성합니다.
prefix_sum = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + array[i-1][j-1]

x1y1x2y2= []
for i in range(m) :
    x1y1x2y2.append(list(map(int, sys.stdin.readline().split())))
    
for i in range(m):
    x1, y1, x2, y2 = x1y1x2y2[i]
    result = prefix_sum[x2][y2] - prefix_sum[x2][y1-1] - prefix_sum[x1-1][y2] + prefix_sum[x1-1][y1-1]
    sys.stdout.write(str(result)+ '\n')
