import math
testcase = int(input())



for j in range (testcase) :
    
    
    dist_cur, dist_goal = map(int,input().split())
    distance = dist_goal - dist_cur
    
    if (distance == 1) :
        print(1)
        continue
    elif (distance == 2) :
        print(2)
        continue
    elif (distance == 3) :
        print(3)
        continue
    elif (distance == 4) :
        print(3)
        continue
            
    for i in range (3, math.ceil(math.sqrt(distance)) + 1) :

        if (distance <= i ** 2) :
            if (distance == i ** 2) :
                print(i + (i-1))
                # print('정확히', i, '정수배에 걸렸어요 :)')
                continue
                
            elif (distance > (i-1) ** 2 and distance < i ** 2) :
                
                if (distance <= i ** 2 - i) :
                    print(2 * (i-1))
                    # print(i-1, '과', i, '사이에 걸렸어요! 그리고 사이의 절반보다 작아요')
                    continue
                
                else :
                    print(i + (i - 1))
                    # print(i-1, i, '사이의 절반보다 커요')
                    continue
            
# 틀린 이유 : i를 ++ 시켜주지 않았다.
# + 성질에 대해 정확히 파악하지 못했다.
# 4 와 9 사이에는 4개의 값만 가지는 것이 아니라
# 중간으로 나누어 5,6 은 4개
# 7, 8은 5개의 값을 가졌다.

# 그리고 조건문을 조금 더 간추릴 수 있지 않을까 생각해본다.