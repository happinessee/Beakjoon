def hanoi(n, start, to, dir):
    if n == 1:
        print(start, to)
    else:
        hanoi(n-1, start, dir, to)
        print(start, to)
        hanoi(n-1, dir, to, start)

n = int(input())
print(2**n - 1)
hanoi(n, 1, 3, 2)