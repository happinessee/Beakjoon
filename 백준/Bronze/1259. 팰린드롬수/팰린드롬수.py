import sys

def is_palindrome(num) :
	tmp = str(num)
	for i in range (len(tmp) // 2) :
		if (tmp[i] != tmp[-(i + 1)]) :
			return (False)
	return (True)

while (1) :
	num = int(sys.stdin.readline())
	if (num == 0) :
		break
	if (is_palindrome(num)) :
		print("yes")
	else :
		print("no")