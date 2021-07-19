arr = list(input())
arr.sort(reverse=True)
tmp = ''
for i in range(len(arr)) :
    tmp += arr[i]
print(tmp)