data = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

data_b = bytes.fromhex(data)

'''
print(len(data_b))

std_str = "crypto{}"
res = []
for i in range(-1, len(std_str)-1):
	for a in range(0,255):
		if chr(data_b[i]^a) == std_str[i]:
			res.append(chr(a))

temp = res.pop(0)
res.append(temp)
print(res, len(res))
print("Done")
'''

# 8 characters is the possible key length from above the above code,
# "myXORke" being the first 7 characters
# a decent guess for the key would be "myXORkey"

key = 'myXORkey'
res = ""
for i in range(0, len(data_b)):
	index = i % 8
	res = res + chr(data_b[i] ^ ord(key[index]))
print(res)
 
