with open("links.txt") as f:
    lines = f.readlines()

for line in lines:
	for word in line.split(' '):
		if word[:len("https://")] == "https://":
			print "0. [" + word[:-1] + "]" + "(" + word[:-1] + '){:target="_blank"}\n'
		else:
			print word,

# for line in lines:
# 	lin = ""
# 	for char in line:
		# if char == '[':
		# 	lin += '('
		
		# elif char == '(':
		# 	lin += '['
		
		# elif char == ']':
		# 	lin += ')'

	# 	if char == ')':
	# 		lin += '){:target="_blank"}'
	# 	else:
	# 		lin += char
	# print lin,