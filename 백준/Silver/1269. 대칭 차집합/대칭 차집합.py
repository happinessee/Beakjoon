import sys

n, m = map(int, sys.stdin.readline().split())
arr1 = set(map(int, sys.stdin.readline().split()))
arr2 = set(map(int, sys.stdin.readline().split()))

print(len((arr1 - arr2) | (arr2 - arr1)))