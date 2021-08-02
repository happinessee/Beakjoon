n, m = map(int, (input().split()))

arr = []
for i in range(1, n+1) :
    arr.append(i)

v = []
select = [False] * 83

def printFunc() :
    for i in range(n) :
        if (select[i]) :
            print(arr[i], end = " ")
    print()

def dfs(idx, cnt) :
    if (cnt == m) :
        printFunc()
        return

    for i in range(idx, n) :
        if(select[i] == True) :
            continue

        select[i] = True
        dfs(i + 1, cnt + 1)
        select[i] = False

dfs(0, 0)