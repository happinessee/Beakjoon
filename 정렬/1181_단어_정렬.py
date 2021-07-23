import sys
n = int(sys.stdin.readline())

word_arr = set([])
for i in range(n) :
    word_arr.add(sys.stdin.readline().strip())
word_list = list(word_arr)
word_list.sort()
word_list.sort(key= len)

for i in range(len(word_arr)) :
    print(word_list[i])