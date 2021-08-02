m, n = map(int, (input().split()))

arr = []
for i in range(1, m+1) :
    arr.append(i)


v = []
select = [False] * m

def printFunc() :
    for i in range(len(v)) :
        print(v[i], end = " ")
    print()

def dfs(cnt) :
    if (cnt == n) :
        printFunc()
        return

    for i in range(m) :
        # if(select[i] == True) :
        #     continue

        select[i] = True
        v.append(arr[i])
        dfs(cnt + 1)
        v.pop()
        select[i] = False

dfs(0)