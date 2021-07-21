n = int(input())
arr = []
for i in range(n) :
    arr.append(int(input()))

arr.sort()
# 1. 산술평균
avg = round(sum(arr) / len(arr))
print(avg)

# 2. 중앙값
print(arr[n//2])

# 3. 최빈값
count = []
for i in range(n) :
    

# 4. 범위
print(arr[n-1] - arr[0])