import sys

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None

n, m = map(int, sys.stdin.readline().split())
while(n != 0 and m != 0):
    n_list, m_list = [], []
    for i in range(n):
        n_list.append(int(sys.stdin.readline()))
    for i in range(m):
        m_list.append(int(sys.stdin.readline()))
    cnt = 0
    for i in n_list:
        if (binary_search(m_list, i) != None):
            cnt += 1
    print(cnt)
    n, m = map(int, sys.stdin.readline().split())
    
