n = int(input())

case = []
for i in range(n) :
    case.append(list(input().split()))
    tmp = float(case[i][0])
    for j in range (1, len(case[i])) :
        
        if (case[i][j] == '@') :
            tmp *= 3
        elif (case[i][j] == '%') :
            tmp += 5
        else :
            tmp -= 7

    print('%.2f' %round(tmp,2))


