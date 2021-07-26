# 피사노 주기 = 파보나치 수를 구하는 또 다른 방법
n = int(input())
cycle = 1500000

fibo = [0 for i in range(cycle)]
fibo[0] = 0
fibo[1] = 1


for i in range(2, cycle) :
    fibo[i] = fibo[i-2] + fibo[i-1]
    fibo[i] = fibo[i] % 1000000

print(fibo[n%cycle])