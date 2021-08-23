t = int(input())

stack = []

for i in range(t) :
    tmp = input()

    for j in range(len(tmp)) :
        if tmp[j] == '(' :
            stack.append('(')

        else :
            if (len(stack) >= 1) :
                stack.pop()
            
            else :
                print("NO")
                break
        
    if (len(stack) == 0) :
        print("YES")

    else :
        print("NO")