import sys
while(True) :
    result = True
    stack = []

    tmp = sys.stdin.readline().rstrip("\n")
    if (tmp == '.') :
        break
    
    for i in tmp :
        
        if i == '(' :
            stack.append(0)
        
        elif i == '[' :
            stack.append(1)

        elif i == ')' :
            if (len(stack) >= 1) :
                a = stack.pop()
                if (a != 0) :
                    result = False
            else :
                result = False

        elif i == ']' :
            if (len(stack) >= 1) :
                b = stack.pop()
                if (b != 1) :
                    result = False
            else :
                result = False
    
    if (len(stack) != 0) :
        result = False

    if (result == True) :
        print("yes")
    else :
        print("no")