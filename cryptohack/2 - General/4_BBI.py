a = "string"
y =""
for x in a:
	xx = ord(x)
	y = y + hex(xx).lstrip('0x')
print(y)
print(int(y, 16))

input_num = "11515195063862318899931685488813747395775516287289682636499965282714637259206269"

print(input_num.encode())

hex_form = hex(int(input_num))[2:]
print(hex_form)
print(type(hex_form))
Byte_form = bytes.fromhex(hex_form)

print(Byte_form.decode('ASCII'))

