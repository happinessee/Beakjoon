import sys

def roundTraditional(val, digits):
    return round(val+10**(-len(str(val))-1), digits)

n = int(sys.stdin.readline())
if (n != 0) :
	levelList = []
	for i in range(n) :
		levelList.append(int(sys.stdin.readline()))
	percent15 = int(roundTraditional(n * 0.15, 0))
	levelList.sort()
	if (percent15 < 1) :
		tmp = sum(levelList)
	else:
		tmp = sum(levelList[percent15: -percent15])
	sys.stdout.write(str(int(roundTraditional(tmp/(n - 2*percent15),0))))
else :
	sys.stdout.write("0")

