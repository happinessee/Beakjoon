import sys
import heapq

t = int(sys.stdin.readline())
heap = []

for i in range (t) :
	tmp = int(sys.stdin.readline())
	if (tmp == 0) :
		if (len(heap) == 0) :
			print(0)
		else :
			print(heapq.heappop(heap)[1])
	else :
		heapq.heappush(heap, (abs(tmp), tmp))
