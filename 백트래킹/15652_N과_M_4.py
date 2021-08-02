m, n = map(int, (input().split()))

arr = []
select = [False] * m
for i in range(1, m+1) :
    arr.append(i)

v = []

def printFunc() :
    for i in range(len(v)) :
        print(v[i], end = " ")
    print()

def dfs (idx, cnt) :
    if (cnt == n) :
        printFunc()
        return

    for i in range(idx, m) :

        v.append(arr[i])
        dfs(i, cnt+1)
        v.pop()

dfs(0,0)