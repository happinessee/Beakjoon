import sys
stack = []
n = int(sys.stdin.readline())

for i in range(n) :
    
    tmp = sys.stdin.readline().strip()

    if (tmp == 'top') :
        print(stack[len(stack) -1]) if len(stack) >= 1 else print(-1)

    elif (tmp == 'size') :
        print(len(stack))

    elif (tmp == 'pop') :
        print(stack.pop()) if len(stack) >= 1 else print(-1)

    elif (tmp == 'empty') :
        print(1 if len(stack) == 0 else 0)

    else :
        stack.append(tmp[5:])