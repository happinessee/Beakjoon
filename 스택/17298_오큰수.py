import sys
n = int(sys.stdin.readline())

stack = list(map(int, sys.stdin.readline().split()))
answer = []

for i in range(n) :
    j = i + 1
    while(True) :

        if (j == len(stack)) :
            answer.append(-1)
            break

        if (stack[i] < stack[j]) :
            answer.append(stack[j])
            break

        else :
            j += 1
            
for i in range(n) :
    print(answer[i], end=" ")