from pwn import * # pip install pwntools
import json
import base64
import codecs


r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)

while(True):
	to_send = {}

	received = json_recv()

	#print(received) #Not required as debug is on

	json_recv_headers = []

	for i in received.keys():
		json_recv_headers.append(i)

	if len(json_recv_headers) == 2 and json_recv_headers[1] == "encoded":
		data = received["encoded"]
		res = ""
		if received["type"] == "base64":
			base64_bytes = data.encode('ascii')
			message_bytes = base64.b64decode(base64_bytes)
			res = message_bytes.decode('ascii')
			
		elif received["type"] == "hex":
			hex_bytes = bytes.fromhex(data)
			res = hex_bytes.decode("ASCII")
		
		elif received["type"] == "rot13":
			res = codecs.encode(data, 'rot_13')
		elif received["type"] == "bigint":
			hex_form = data[2:]
			hex_bytes = bytes.fromhex(hex_form)
			res = hex_bytes.decode("ASCII")
			
		elif received["type"] == "utf-8":
			for Data in data:
				res = res + chr(Data)
		print(res)
		to_send["decoded"] = res
		json_send(to_send)
	else:
		break

print("Game-over")
