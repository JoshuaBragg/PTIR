import sys
for i in range(16):
	for j in range(16):
		ind = i * 16 + j
		code = str(ind)
		if ((ind + 8) % 6 == 0 and 232 > ind > 15) or ind == 16 or ind == 232:
			print(u"\u001b[0m")
		sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
print(u"\u001b[0m")
