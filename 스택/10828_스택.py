stack = []

n = int(input())

for i in range(n) :

    if (tmp == 'push') :
        tmp, num = input().split()

    else :
        tmp = input()

    if (tmp == 'push') :
        stack.append(num)

    if (tmp == 'top') :
        print(stack[len(stack) -1]) if len(stack) >= 1 else print(-1)

    if (tmp == 'size') :
        print(len(stack))

    if (tmp == 'pop') :
        stack.pop() if len(stack) >= 1 else print(-1)

    if (tmp == 'empty') :
        print(1 if len(stack) == 0 else 0)
