import sys

melody = list(map(int, sys.stdin.readline().split()))

is_sorted = all(x <= y for x, y in zip(melody[:-1], melody[1:]))
if (is_sorted) :
	print("ascending")
	exit()
is_sorted = all(x >= y for x, y in zip(melody[:-1], melody[1:]))
if (is_sorted) :
	print("descending")
else :
	print("mixed")