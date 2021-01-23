from decimal import Decimal

# n=お酒の杯数、 x=アルコール限界値ml
s = input().split()
n = int(s[0])
x = int(s[1])

now = 0
out = False

for i in range(n):
	# v=量ml、 p=アルコール度数%
	s = input().split()
	v = int(s[0])
	p = int(s[1])
	alc = Decimal(v) * (Decimal(p) / Decimal(100))
	now = Decimal(now) + Decimal(alc)

	if Decimal(x) < Decimal(now):
		print(i+1)
		out = True
		break

if out == False:
	print(-1)
