hour, minute, sec = map(int, input().split())
need_sec = int(input())

tmp = need_sec // 3600
tmp1 = (need_sec%3600) // 60
tmp2 = need_sec % 60

sec += tmp2
minute += tmp1
hour += tmp

if (sec >= 60) :
    sec -= 60
    minute += 1

if (minute >= 60) :
    minute -= 60
    hour += 1

if (hour >= 24) :
    hour %= 24

print(hour, minute, sec)