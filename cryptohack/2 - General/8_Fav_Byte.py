data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"

data_b = bytes.fromhex(data)

print(len(data_b))

for i in range(0,255):
	res = ""
	for a in range(0,len(data_b)):
		res = res + chr(i ^ data_b[a])
	print(res)
print("Done")
