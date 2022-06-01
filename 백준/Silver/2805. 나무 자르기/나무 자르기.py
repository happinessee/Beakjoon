import sys

n, m = map(int, sys.stdin.readline().split())
tree_set = list(map(int, sys.stdin.readline().split()))
tree_set.sort()

start = 0
end = max(tree_set)
res = 0
while (start <= end) :
	tmp = 0
	mid = (start + end) // 2
	for i in range (len(tree_set)) :
		if (tree_set[i] > mid) :
			tmp += tree_set[i] - mid
	if (tmp >= m) :
		res = mid
		start = mid + 1
	else :
		end = mid - 1

print(res)
