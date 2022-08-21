import sys

# k 1 q 1 l 2 v 2 kn 2 p 8
k, q, l, v, kn, p = map(int, (sys.stdin.readline().split()))
white_k, white_q, white_l, white_v, white_kn, white_p = 0, 0, 0, 0, 0, 0

if (k != 1):
	while(k != 1):
		if (k < 1):
			white_k += 1
			k += 1
		else:
			white_k -= 1
			k -= 1

if (q != 1):
	while(q != 1):
		if (q < 1):
			white_q += 1
			q += 1
		else:
			white_q -= 1
			q -= 1

if (l != 2):
	while(l != 2):
		if (l < 2):
			white_l += 1
			l += 1
		else:
			white_l -= 1
			l -= 1

if (v != 2):
	while(v != 2):
		if (v < 2):
			white_v += 1
			v += 1
		else:
			white_v -= 1
			v -= 1

if (kn != 2):
	while(kn != 2):
		if (kn < 2):
			white_kn += 1
			kn += 1
		else:
			white_kn -= 1
			kn -= 1

if (p != 8):
	while(p != 8):
		if (p < 8):
			white_p += 1
			p += 1
		else:
			white_p -= 1
			p -= 1

print(white_k, white_q, white_l, white_v, white_kn, white_p)