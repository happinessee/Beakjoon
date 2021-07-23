# 빛의 속도
c = 299792458.0

a, b = (input().split())
a = float(a)
b = float(b)

# 상대속도 공식 + 상대오차 10^-9 이하로 만들어주기 위해 반올림
temp = round((a + b) / (1 + (a * b) / (c * c)), 12)

print(temp)