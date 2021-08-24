import sys

n = int(sys.stdin.readline())
result = True
count = 1
stack = []
answer = []

for i in range(n) :
    k = int(sys.stdin.readline())

    while(k >= count) :
        stack.append(count)
        count += 1
        answer.append('+')
    
    if (k == stack[-1]) :
        stack.pop()
        answer.append('-')

    else :
        result = False

if (result == True) :
    for i in answer :
        print(i)
else :
    print('NO')