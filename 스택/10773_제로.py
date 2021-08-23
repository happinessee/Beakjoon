stack = []

k = int(input())

for i in range(k) :

    tmp = int(input())
    
    if (tmp == 0) :
        stack.pop()

    else :
        stack.append(int(input()))

answer = 0
for i in range(len(stack)) :
    answer += stack[i]

print(answer)