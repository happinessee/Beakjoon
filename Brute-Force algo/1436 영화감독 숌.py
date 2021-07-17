n = int(input())

start = 665
count = 0
while (count != n) :
    start += 1
    if (str(start).find('666') != -1) :
        count += 1

print(start)
