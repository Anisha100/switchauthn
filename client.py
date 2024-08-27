import hmac
import hashlib
import socket
from time import sleep
import time
key=input("key")
challenge=''	
def get_ch():	
	#get challenge
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	sock.bind(("192.168.29.255", 5005))
	sock.settimeout(10)

	while True:
		challenge, addr = sock.recvfrom(1024)
	sock.close()
	#type is strings, generate CK1
	#challenge=challenge.content
	signed=hmac_sha256(key,challenge)
	print(signed)
	
	#broadcast CK1
	#interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
	#allips = [ip[-1][0] for ip in interfaces]
	msq=signed
	print(f'sending on {msg}')
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	sock.bind('192.168.29.255',5005)
	sock.settimeout(10)
	while True:
			print(msg,len(msg))
			sock.sendto(msg, ("192.168.29.255", 5005))
			time.sleep(1)
	sock.close()
		
def hmac_sha256(key, message):
  return hmac.new(
    key.encode("utf-8"), 
    message.encode("utf-8"), 
    hashlib.sha256
  ).hexdigest()
  
get_ch()
		
		