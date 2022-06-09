import sys

n = int(sys.stdin.readline())
fac = []
fac.append(1)
fac.append(1)
fac.append(2)
for i in range (3, n + 1) :
	fac.append(i * fac[i - 1])

tmp_st = str(fac[n])
cnt = 0
for i in tmp_st[::-1] :
	if (i == '0') :
		cnt += 1
	else :
		break

print(cnt)
