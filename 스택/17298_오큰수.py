import sys
n = int(sys.stdin.readline())

stack = list(map(int, sys.stdin.readline().split()))


answer = []

i = 0
j = 1
while(True) :
    if (stack[i] < stack[j]) :
        answer.append(stack[j])
    else :
        
        

answer.append(-1)
            
for i in range(n) :
    print(answer[i], end=" ")