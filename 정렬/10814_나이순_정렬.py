import sys
n = int(sys.stdin.readline())

member = []
for i in range(n) :
    member_age, member_name = sys.stdin.readline().strip().split()
    member.append([int(member_age), member_name])

member.sort(key= lambda x : x[0])
for i in range(n) :
    print(member[i][0], member[i][1])