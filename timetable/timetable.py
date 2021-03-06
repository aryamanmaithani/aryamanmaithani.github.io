__author__ = 'Aryaman Maithani'

with open("timetable.txt") as f:
    lines = f.read().splitlines()

def assign(s1, s2):
	if s1 != 'x':
		return s1
	if s2 != 'x':
		return s2
	return ''

def makeEntry(slot):
	particular = dicc[slot]
	parent = dicc[par[slot]]
	course = ""
	location = ""
	course = assign(particular[0], parent[0])
	location = assign(particular[1], parent[1])
	return "\\entry{" + course + "}{" + location + "}"

dicc = {}
for line in lines:
	if line[:3] == "===":
		continue
	chunk = line.split(">>")
	dicc[chunk[0]] = [chunk[1], chunk[2]]

par = {} 		# parent codes
for i in range(1, 16):			
	for ch in ['A', 'B', 'C']:  # Yes, I know not all courses have C
		par[str(i) + ch] = str(i)
for ch in "123CD":
	par['X' + ch] = 'X' + ch

tt = [#
		["1A", "2A", "3A", "4A", "8A", "9A", "12A", "13A"],
		["4B", "1B", "2B", "3B", "10A", "11A", "14A", "15A"],
		["7A", "5A", "6A", "X1", "X2", "X3", "XC", "XD"],
		["3C", "4C", "1C", "2C", "8B", "9B", "12B", "13B"],
		["7B", "5B", "6B", "10B", "11B", "14B", "15B"],
	]

def normalDay(name, number):
	row = name + " "
	for slot in tt[number]:
		row += "& " + makeEntry(slot) + " "
	row += "\\\\"
	return row + "\n\\hline"

def wed():
	row = "Wednesday "
	T = tt[2]
	row += "& " + makeEntry(T[0]) + " "
	row += "& \\multicolumn{3}{c||}{\\begin{tabular}{l|r} \\hspace{-0.6cm}"
	row += makeEntry(T[1])
	row += "\\hspace{0.6cm} & \\hspace{0.6cm} "
	row += makeEntry(T[2])
	row += "\\hspace{-0.6cm} \\end{tabular}} "
	row += "& \\multicolumn{2}{c||}{\\begin{tabular}{c|c|c} "
	row += makeEntry(T[3])
	row += " & \\hspace{0.3cm} "
	row += makeEntry(T[4]) + "\\hspace{0.3cm}  & "
	row += makeEntry(T[5]) + " \\end{tabular}}"
	for i in range(6, len(T)):
		row += "& " + makeEntry(T[i]) + " "
	row += "\\\\"
	return row + "\n\\hline"

def fri():
	row = "Friday "
	T = tt[4]
	row += "& " + makeEntry(T[0]) + " "
	row += "& \\multicolumn{3}{c||}{\\begin{tabular}{l|r} \\hspace{-0.6cm}"
	row += makeEntry(T[1])
	row += "\\hspace{0.6cm} & \\hspace{0.6cm} "
	row += makeEntry(T[2])
	row += "\\hspace{-0.6cm} \\end{tabular}} "
	for i in range(3, len(T)):
		row += "& " + makeEntry(T[i]) + " "
	row += "\\\\"
	return row + "\n\\hline"

print ("\\hline")
print (normalDay("Monday", 0))
print (normalDay("Tuesday", 1))
print (wed())
print (normalDay("Thursday", 3))
print (fri())