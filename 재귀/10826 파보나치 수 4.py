# 재귀함수로는 메모리 초과, 시간 초과로 풀리지 않는다. fibonacci의 10000 번째 수는 생각보다 훨씬 더 큰 수였다..
# 이런 식으로 정보를 저장하며 풀어나가는 것을 동적계획법(Dynamic Programming)이라고 했다.
def fibonacci(count) :
    first_num = 0
    second_num = 1

    for i in range(count) :
        first_num, second_num = second_num, (first_num + second_num)

    return first_num

n = int(input())

if(n == 0) :
    print(0)
elif(n==1) :
    print(1)
else :
    result = fibonacci(count= n)
    print(result)