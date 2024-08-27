#from flask import Flask, request, render_template
import requests
import hmac
import hashlib
import socket
from time import sleep
import time
#app=Flask(__name__)
key=input("KEY")
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
        sock.bind(('192.168.29.255',5005))
        sock.settimeout(10)
        while True:
            print(msg,len(msg))
            sock.sendto(msg, ("192.168.29.255", 5005))
            time.sleep(1)
        sock.close()

        #type is strings, challenge hashed with K2=CK2
        challenge=challenge.content
        signed=hmac_sha256(key,challenge)
        
        #receiving CK1
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPRONTO_UDP)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.bind("192.168.29.255", 5005)
        while True:
            ck1, addr = sock.recvfrom(1024)
            if(ck1==challenge):
                print("verified")
        


    #return render_template("admin.html")
    
def hmac_sha256(key, message):
  return hmac.new(
    key.encode("utf-8"),
    message.encode("utf-8"),
    hashlib.sha256
  ).hexdigest()
 

get_key()
#if __name__ == '__main__':
#    app.run()
