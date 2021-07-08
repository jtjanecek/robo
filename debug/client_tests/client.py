#! /home/fourbolt/anaconda3/bin/python


import json
import socket
import threading
import socketserver
import time

def client(ip, port, packets):
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
		sock.connect((ip, port))
		for packet in packets:
			if packet['src'] == '10078' or packet['dst'] == '10078':
				break
			if packet['dst'] == '10075': # Send
				hex_string = packet['data']
				print(f"Sending: {hex_string}")
				sock.sendall(bytes.fromhex(hex_string))
			else: # Recv
				response = sock.recv(1024).hex().upper()
				while (response == ''):
					response = sock.recv(1024).hex().upper()
				if response != packet['data']:
					print(f"Response: {response}")
					print(f"Expected: {packet['data']}")
					raise AssertionError
				print("Received: {}".format(response))
				
			time.sleep(.5)	

def read_packets():
	with open('client_tests/packets.json', 'r') as f:
		packets = f.read()
	packets = json.loads(packets)

	final = []
	for packet in packets:
		data = packet['_source']['layers']['data']['data.data'].replace(":","").upper()
		dstPort = packet['_source']['layers']['tcp']['tcp.dstport']
		srcPort = packet['_source']['layers']['tcp']['tcp.srcport']

		final.append({'src':srcPort,'dst':dstPort,'data':data})	
	return final

if __name__ == "__main__":
	# Port 0 means to select an arbitrary unused port

	port = 10075
	ip = '192.168.1.2'

	packets = read_packets()

	client(ip, port, packets)

	#client(ip, port, "Hello World 2")
	#client(ip, port, "Hello World 3")


# j[0]['_source']['layers']['data']['data.data'].replace(":","").upper()

