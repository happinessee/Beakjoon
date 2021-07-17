# 제대로 작동하는지 check해보고, 고치는데 어느정도.
# 그리고 방금 깨달았는데, if문의 순서를 제대로 넣지 않아서 시간이 어느정도 또 들었다.
# 조건문의 순서 확실히 생각해보자

# + 시간 초과가 발생한다 어떤 점을 줄일 수 있을까??

n , m = map(int, input().split())

chessboard = [[] * m ] * n

# 체스판의 값을 입력받음
for i in range(n) :
    tmp_arr = list(input())
    chessboard[i] = (tmp_arr)
    

k = 0
l = 0
tmp2 = 65

while(True) :
    changeCount_B = 0
    changeCount_W = 0

    for i in range (4) :
        qq = i * 2

        for j in range (4) :
            pp = j * 2
                
            if (chessboard[qq + k][pp + l] == 'W') :
                    changeCount_B += 1
                
            if (chessboard[qq + k][pp + 1 + l] == 'B') :
                    changeCount_B += 1
                
            if (chessboard[qq + 1 + k][pp + l] == 'B') :
                    changeCount_B += 1
                    
            if (chessboard[qq + 1 + k][pp + 1 + l] == 'W') :
                    changeCount_B += 1


            if (chessboard[qq + k][pp + l] == 'B') :
                    changeCount_W += 1
                
            if (chessboard[qq + k][pp + l + 1] == 'W') :
                    changeCount_W += 1
                
            if (chessboard[qq + 1 + k][pp + l] == 'W') :
                    changeCount_W += 1
                    
            if (chessboard[qq + 1 + k][pp + 1 + l] == 'B') :
                    changeCount_W += 1

    tmp = min(changeCount_W, changeCount_B)

    if(tmp < tmp2) :
        count_min = tmp
        tmp2 = count_min
    
    if (l < m - 7) :
        l += 1
    
    if (l == m - 7) :
        l = 0
        k += 1
            
        if (k > n - 8) :
            break

print(count_min)