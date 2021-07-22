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
count = 0
count_cont = 0
arr_temp = []
for i in range(len(arr)) :
    if (count_cont >= 1) :
        count_cont -= 1
        continue

    if (count == arr.count(arr[i])) :
        arr_temp.append(arr[i])
        count_cont = count - 1

    if (count < arr.count(arr[i])) :
        count = arr.count(arr[i])
        count_cont = count - 1
        arr_temp.clear()
        arr_temp.append(arr[i])


if (len(arr_temp) >= 2) :
    arr_temp.sort()
    print(arr_temp[1])

else :
    print(arr_temp[0])

# 4. 범위
print(arr[n-1] - arr[0])