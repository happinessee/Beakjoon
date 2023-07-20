import sys

n = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))

result = []
for i in range(1, len(students) + 1):
    result.insert(students[i - 1], i)

for i in range(len(result)-1, 0, -1):
    sys.stdout.write(str(result[i]))
    sys.stdout.write(" ")
sys.stdout.write(str(result[0]))
