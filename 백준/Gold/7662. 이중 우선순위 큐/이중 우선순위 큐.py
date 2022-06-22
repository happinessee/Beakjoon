import sys
import heapq

t = int(sys.stdin.readline())
for i in range (t) :
	min_heap = []
	max_heap = []
	deleted = [0] * 1000001
	n = int(sys.stdin.readline())

	for j in range (n) :
		comm, num = sys.stdin.readline().split()
		num = int(num)
		if (comm == 'I') :
			heapq.heappush(min_heap, (num, j))
			heapq.heappush(max_heap, (-num, j))
		else :
			if (num == -1) :
				while (min_heap and deleted[min_heap[0][1]]) :
					heapq.heappop(min_heap)
				if (min_heap) :
					deleted[min_heap[0][1]] = 1
					heapq.heappop(min_heap)
			else :
				while (max_heap and deleted[max_heap[0][1]]) :
					heapq.heappop(max_heap)
				if (max_heap) :
					deleted[max_heap[0][1]] = 1
					heapq.heappop(max_heap)
	while (min_heap and deleted[min_heap[0][1]]) :
		heapq.heappop(min_heap)
	while (max_heap and deleted[max_heap[0][1]]) :
		heapq.heappop(max_heap)
	if (min_heap and max_heap) :
		sys.stdout.write(str(-max_heap[0][0]) + ' ' +  str(min_heap[0][0]) + '\n')
	else :
		sys.stdout.write("EMPTY\n")