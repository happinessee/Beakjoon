import sys

s = sys.stdin.readline().rstrip('\n')
idx = 1
str_set = set()
cnt = 0

while (True) :
	str_set.add(s[cnt : cnt + idx])
	cnt += 1
	if (idx == len(s)) :
		break
	if ((cnt + idx) == (len(s) + 1)) :
		cnt = 0
		idx += 1
print(len(str_set))
