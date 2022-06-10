import sys
tmp = sys.stdin.readline().rstrip('\n')
res = ''
for i in tmp :
	if (ord(i) >= 65 and ord(i) <= 90) :
		res += chr(ord(i) + 32)
	else :
		res += chr(ord(i) - 32)
print(res)
