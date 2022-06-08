import sys

st = sys.stdin.readline().rstrip('\n')
tmp = ""
tmp_num = 0

sign = 1
buffer = ''
for i in st :
	if (i >= '0' and i <= '9') :
		buffer += i
	else :
		tmp_num += (int(buffer) * sign)
		if (i == '-') :
			sign = -1
		buffer = ''
tmp_num += (int(buffer) * sign)

print(tmp_num)
