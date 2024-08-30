#from flask import Flask, request, render_template
import requests
import hmac
import hashlib
import socket
from time import sleep
import time
#import threading

#app=Flask(__name__)
key=input("KEY")
#challenge=requests.get("https://www.uuidgenerator.net/api/version1")
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
#sock.bind(('192.168.29.255',5005))

#@app.route('/', methods=['GET'])
def get_key():
#    if request.method == 'GET':
    
        #k2 received
#        key=request.args.get("key")
        
        #challenge generated
        challenge=requests.get("https://www.uuidgenerator.net/api/version1")
        
        #challenge broadcasted
        #interfaces = socket.getaddrinfo(host=socket.gethostname(), port=None, family=socket.AF_INET)
        ip = '192.168.29.248'
        msg=challenge.content
        print(f'sending on {ip}')
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)  # UDP
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind(('',5005))
        #sock.settimeout(10)
        print(msg,len(msg))
        sock.sendto(msg, ("192.168.29.255", 5005))
#        time.sleep(10)
        sock.close()
#def receive():
        #type is strings, challenge hashed with K2=CK2
        #msg2=challenge.content
        signed=(hmac_sha256(key,msg)).encode()
        
        #receiving CK1
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind(("", 6005))
        while True:
            try:
                ck1, addr = sock.recvfrom(1024)
                if(ck1==signed):
                    print(f'The received chslleneg is : {ck1} and received challenge is {signed}')
                    print("verified")
                else:
                    print(f'signed challenge from client is {ck1} and signed challenge in server is {signed}')
            except:
                pass


    #return render_template("admin.html")
    
def hmac_sha256(key, message):
  return hmac.new(
    key.encode("utf-8"),
    message,
    hashlib.sha256
  ).hexdigest()
 
#t1=threading.Thread(target=get_key)
#t2=threading.Thread(target=receive)
#t1.start()
#t2.start()
get_key()


#if __name__ == '__main__':
#    app.run()
