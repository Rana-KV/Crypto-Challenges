import base64

a = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

b_string = bytes.fromhex(a)

b64_string = base64.b64encode(b_string)

print(b64_string)
