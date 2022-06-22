import sys

n = int(sys.stdin.readline())
s = int(sys.stdin.readline())
st = sys.stdin.readline().rstrip('\n')

lst = []
idx = 0
flag = 0
res = 0
count = 0
while idx < (s - 1):
    if st[idx : idx + 3] == 'IOI':
        idx += 2
        count += 1
        if count == n:
            res += 1
            count -= 1
    else:
        idx += 1
        count = 0

sys.stdout.write(str(res) + '\n')
