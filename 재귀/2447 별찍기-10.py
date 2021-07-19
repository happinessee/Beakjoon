def star10(n, map, col, row) :
#    print(col, row, "star10 작동")

    for i in range(col, col + n, n//3) :
        for j in range(row,row + n, n//3) :
            if (n != 3) :
                if (i == n//3 + col and j == n//3 + row) :
                    None
                else :
                    map = star10(n = n//3, map = map, col = i, row = j)

            else :
                if (i % 3 == 1 and j % 3 == 1) :
                    map[i][j] = " "
                else :
                    map[i][j] = "*"
    return map

n= int(input())
star = [[' ']*2200 for i in range(2200)]

star10(n=n, map=star, col= 0, row= 0)

for i in range(n) :
    if (i >= 1) :
        print()
    for j in range(n) :
        print(star[i][j], end = "")