KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY1_X_2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2_X_3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAG_X_1_X_2_X_3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

def byte_XOR(a, b, c):
	res = ""
	for aa in range(0,len(a)):
		res = res + chr(a[aa]^b[aa]^c[aa])
	return res

# hex to binary

Key1_b = bytes.fromhex(KEY1)
print(Key1_b, Key1_b[0])
Key1_X_2_b = bytes.fromhex(KEY1_X_2)

Key2_X_3_b = bytes.fromhex(KEY2_X_3)

Flag_X_1_X_2_X_3_b = bytes.fromhex(FLAG_X_1_X_2_X_3)

print(byte_XOR(Key1_b,Flag_X_1_X_2_X_3_b, Key2_X_3_b))

