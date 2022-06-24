from cmath import e
import sys

n = int(sys.stdin.readline())
R = []
G = []
B = []
for i in range (n) :
	tmp = list(map(int, sys.stdin.readline().split()))
	R.append(tmp[0])
	G.append(tmp[1])
	B.append(tmp[2])

dp = [[0, 0, 0] for _ in range (n)]
dp[0][0] = R[0]
dp[0][1] = G[0]
dp[0][2] = B[0]
for i in range (1, n) :
	dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + R[i]
	dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + G[i]
	dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + B[i]

print(min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2]))
