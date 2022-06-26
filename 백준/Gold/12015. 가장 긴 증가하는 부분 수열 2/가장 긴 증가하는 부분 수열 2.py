import bisect, sys

x = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

dp = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))