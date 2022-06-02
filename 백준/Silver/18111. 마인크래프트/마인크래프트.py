import sys

n, m, b = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for i in range (n)]

height = 0
answer = 9999999999999999999

for i in range (257) :
	tmp_get = 0
	tmp_lost = 0
	for j in range (n) :
		for k in range (m) :
			if (i > ground[j][k]) :
				tmp_lost += i - ground[j][k]
			else :
				tmp_get += ground[j][k] - i
	if (tmp_get + b < tmp_lost) :
		continue
	time = 2 * tmp_get + tmp_lost
	if (time <= answer) :
		answer = time
		height = i

print(answer, height)
