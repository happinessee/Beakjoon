# Error 1 시간 초과 문장
import sys

n = int(sys.stdin.readline())

comp = list(map(int, (sys.stdin.readline().split())))

comp_change = sorted(comp)

count = 0
answer = [0 for _ in range(n)]

for i in range(1, n):
    if (comp_change[i - 1] == comp_change[i]) :
        None
    else :
        count += 1
    answer[i] = count

# 시간 초과가 발생해 O(log n)의 탐색방법을 사용하기로 결정.
# 이진 탐색 (Binary Search)
import bisect
for i in range(n) :
    # comp[comp.index(comp_change[i])] = answer[i]
    # 수정한 문장 1개.
    comp[i] = answer[bisect.bisect(comp_change, comp[i]) - 1]

for i in range(n) :
    print(comp[i], end=' ')