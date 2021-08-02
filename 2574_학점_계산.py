n = input()
tmp = 0.0
if (n[0] == 'A'):
    tmp += 4.0
elif (n[0] == 'B') :
    tmp += 3.0
elif (n[0] == 'C') :
    tmp += 2.0
elif (n[0] == 'D') :
    tmp += 1.0
if (len(n) > 1) :    
    if (n[1] == '+') :
        tmp += 0.3
    elif (n[1] == '-') :
        tmp -=0.3
        
print(tmp)