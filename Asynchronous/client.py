import threading 
import hmac
import hashlib
import socket
from time import sleep
import time
from uuid import getnode as get_mac

key=input("key")
challenge=''	
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(("", 5005))

def get_ch():	
      challenge, addr = sock.recvfrom(1024)
			print(f'The received challenge is : {challenge}')
		
#type is strings, generate CK1
	#challenge=challenge.content
	signed=hmac_sha256(key,challenge)
	print(signed)
	
	#broadcast CK1
	msg=signed
	print(f'sending on {msg}')
	mac = get_mac()

	while True:
			print(msg.encode(),len(msg))
			sock.sendto(msg.encode(), ("192.168.29.255", 5005),mac)
			time.sleep(1)
	sock.close()
		
def hmac_sha256(key, message):
  return hmac.new(
    key.encode("utf-8"), 
    message, 
    hashlib.sha256
  ).hexdigest()
  
get_ch()
		
		
