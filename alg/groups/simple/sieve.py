N = 200 # order until which you want to check


def primeFac(n):
	PF = []
	p = 2
	while not n == 1:
		if n % p == 0:
			c = 0
			while n % p == 0:
				n /= p
				c += 1
			PF.append([p, c])
		p += 1
	return PF

def mptype(PF):
	m = 1
	for j in range(len(PF)-1):
		m *= (PF[j][0]**PF[j][1])
	return m < PF[len(PF)-1][0]

S = []
for i in range(2, N+1):
	PF = primeFac(i)
	if len(PF) == 1:
		if PF[0][1] == 1:
			print "*", i, ": p group with p =", PF[0][0]
			continue
		print "*", i, ": $$p^n$$ group with p =", PF[0][0], "and n =", PF[0][1]
		continue
	if len(PF) == 2:
		if PF[0][1] == PF[1][1] == 1:
			print "*", i, ": pq group with p =", PF[0][0], "and q =", PF[1][0]
			continue
		if PF[0][1] == 2 and PF[1][1] == 1:
			print "*", i, ": $$p^2q$$ group with p =", PF[0][0], "and q =", PF[1][0]
			continue
		if PF[0][1] == 1 and PF[1][1] == 2:
			print "*", i, ": $$p^2q$$ group with p =", PF[1][0], "and q =", PF[0][0]
			continue
		if PF[0][0] == 2 and PF[1][0] == 3 and PF[1][1] == 1:
			print "*", i, ": $$2^n\\cdot3$$ group with n =", PF[0][1]
			continue
		if PF[0][0] == 2 and PF[1][0] == 3 and PF[0][1] == 2:
			print "*", i, ": $$3^n\\cdot4$$ group with n =", PF[1][1]
			continue
	if len(PF) == 3:
		if PF[0][1] == PF[1][1] == PF[2][1] == 1:
			print "*", i, ": pqr group with p =", PF[0][0], "and q =", PF[1][0], "and r =", PF[2][0]
			continue
	if mptype(PF):
		m = 1
		for j in range(len(PF)-1):
			m *= (PF[j][0]**PF[j][1])
		print "*", i, ": $$mp^n$$ group with m =", m, "and p =", PF[len(PF)-1][0], "and n =", PF[len(PF)-1][1]
		continue
	
	S.append(i)

print ""
print "Remaining orders:", S