import sys

n, m = map(int, sys.stdin.readline().split())
n_list = list(map(int, sys.stdin.readline().split()))
m_list = list(map(int, sys.stdin.readline().split()))

n_list.extend(m_list)
n_list.sort()
print(' '.join(map(str, n_list)))
