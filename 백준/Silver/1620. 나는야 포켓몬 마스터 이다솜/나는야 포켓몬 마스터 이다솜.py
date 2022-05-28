import sys

pocket_dict = {}
n, m = map(int, sys.stdin.readline().split())
for i in range (1, n + 1) :
	pocket_dict[i] = sys.stdin.readline().rstrip('\n')
pocket_dict_re = {v:k for k,v in pocket_dict.items()}

for i in range (m) :
	tmp = sys.stdin.readline().rstrip('\n')
	if (tmp.isdigit()) :
		print(pocket_dict.get(int(tmp)))
	else :
		print(pocket_dict_re.get(tmp))