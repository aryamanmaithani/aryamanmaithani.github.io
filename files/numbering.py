__author__ = 'aryaman'
filein = "trivial.txt"
fileout = "trivial2.txt"

out = open(fileout, 'w')

with open(filein) as f:
    lines = f.readlines()

i = 1
for line in lines:
	out.write(str(i) + ". " + line)
	i += 1