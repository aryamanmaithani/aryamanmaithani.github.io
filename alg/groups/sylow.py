__author__ = 'aryaman'

start = 3		# inclusive
end = 9999		# inclusive
step = 2
filepath = "sylow-odd.txt"

def primeFac(n):
	PF = []
	p = 2
	c = 0
	div = False
	while not n == 1:
		while n % p == 0:
			div = True
			n //= p
			c += 1
		if div:
			PF.append([p, c])
			c = 0
			div = False
		p += 1
	return PF

def npval(PF, p):
	cp = 1				# complimentary part
	for pf in PF:		# calculating cp
		if not pf[0] == p:
			cp *= (pf[0]**pf[1])
	np = []				# list of values
	
	nptest = 1
	while nptest <= cp:
		if cp % nptest == 0:
			np.append(nptest)
		nptest += p

	return np

count = 0
output = ""
n = start
while n <= end:
	PF = primeFac(n)
	if len(PF) > 1:
		np1 = True
		for pf in PF:
			if len(npval(PF, pf[0])) > 1:
				np1 = False
				break
		if not np1:
			count += 1
			output = output + str(n)
			primefac = ""
			data = ""
			for pf in PF:
				primefac += " * "+str(pf[0])+"^"+str(pf[1])
				data += str(pf[0]) + ": " + str(npval(PF, pf[0])) + "\n"
			primefac = primefac[3:]
			output += " = " + primefac + "\n"
			output += data
			output += "===============\n"
	n += step

file = open(filepath, "w")
file.write("There were "+str(count)+" such numbers out of the "+ str((end-start)/2) +" tested.\n===============\n")
file.write(output)