hour, minute = map(int, input().split())
need_Min = int(input())

tmp = need_Min // 60
tmp1 = need_Min % 60

minute += tmp1
hour += tmp
if (minute >= 60) :
    minute -= 60
    hour += 1

if (hour >= 24) :
    hour -= 24

print(hour, minute)