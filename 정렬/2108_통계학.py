import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n) :
    arr.append(int(sys.stdin.readline()))

arr.sort()
# 1. 산술평균
avg = round(sum(arr) / len(arr))
print(avg)

# 2. 중앙값
print(arr[n//2])

from collections import Counter
# 3. 최빈값
if(n==1) :
    print(arr[0])
else :
    cnt = Counter(arr).most_common(2)
    print(cnt[0][0] if cnt[0][1] != cnt[1][1] else cnt[1][0])

# 4. 범위
print(arr[n-1] - arr[0])