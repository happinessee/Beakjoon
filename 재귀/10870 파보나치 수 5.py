def fibonacci(first_num, second_num, count) :
    tmp = first_num + second_num
    count -= 1

    if (count > 0) :
        return fibonacci(first_num = second_num,second_num= tmp, count= count)

    else :
        return tmp

n = int(input())

first = 0
second = 1
if(n == 0) :
    print(0)
elif(n==1) :
    print(1)
else :
    result = fibonacci(first_num= first, second_num= second, count= n - 1)
    print(result)