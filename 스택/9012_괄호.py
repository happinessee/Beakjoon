t = int(input())



for i in range(t) :
    stack = []
    result = True
    
    tmp = input()

    for j in range(len(tmp)) :
    
        if tmp[j] == '(' :
            stack.append('(')

        else :
            if (len(stack) >= 1) :
                stack.pop()
            
            else :
                result = False
                break
    if (len(stack) != 0) :
        result = False

    if (result == True) :
        print("YES")

    else :
        print("NO")