import sys

hash_size = 100
hash_val = 17

def get_hashkey(str) :
	key = 0

	for i in range(len(str)) :
		key = (key * hash_val) + ord(str[i])
	if (key < 0) :
		key *= -1
	return (key % hash_size)

def check_str(str, str_set) :
	key = get_hashkey(str)
	if (str not in str_set[key]) :
		str_set[key].append(str)
	return (str_set)

# main
cnt = 0

n, m = map(int, sys.stdin.readline().split())
str_set = [[] for i in range (hash_size)]

for i in range(n) :
	str_set = check_str(sys.stdin.readline().rstrip('\n'), str_set)

for i in range(m) :
	tmp = sys.stdin.readline().rstrip('\n')
	if (tmp in str_set[get_hashkey(tmp)]) :
		cnt += 1

print (cnt)
