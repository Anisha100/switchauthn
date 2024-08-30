import requests
import hmac
import hashlib
import socket
from time import sleep
import time
import uuid
import threading


key=input("KEY")

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(('',5005))
msg=str(uuid.uuid4()).encode('utf-8')


def get_key():
     #challenge broadcasted
        while True:
                #sock.settimeout(10)
                print(msg,len(msg))
                sock.sendto(msg, ("192.168.29.255", 5005))

def receive():
        signed=(hmac_sha256(key,msg)).encode()
        
        #receiving CK1
        while True:  
             ck1, addr,mac = sock.recvfrom(1024)
             if(ck1==signed):
                    print(f'The MAC ADDRESS of client with verified challange : {mac}')
                    print(f'The received chslleneg is : {ck1} and received challenge is {signed}')
                    print("verified")
                    break
             else:
                    print(f'signed challenge from client is {ck1} and signed challenge in server is {signed}')

    
def hmac_sha256(key, message):
  return hmac.new(
    key.encode("utf-8"),
    message,
    hashlib.sha256
  ).hexdigest()
 
t1=threading.Thread(target=get_key)
t2=threading.Thread(target=receive)
t1.start()
t2.start()
get_key()


#if __name__ == '__main__':
#    app.run()
