data = "label"
res = ""
for a in data:
	res = res + chr(ord(a)^13)

print('crypto{{{0}}}'.format(res))
