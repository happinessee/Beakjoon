n=int(input())
a = list(map(int,input().split()))
m = max(a)
average = 0
for i in range(n) :
    a[i] = a[i] / m * 100
    average += a[i]

print(float(round((average/n),5)))
