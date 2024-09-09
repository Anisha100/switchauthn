import socket

s1=socket.socket()
s2=socket.socket()
port1=4004
port2=5005
ip='20.198.19.177'

def receive():
       while True:  
             s1.connect((ip,port1))
             msg=s1.recv(1024).decode())
             print(msg)
             
                    
def sending():
	while True:
    s2.bind('',port2)
    c,addr=s2.accept()
		msg=input("message :  ")
		c.send(msg)
		
		             
t1=threading.Thread(targe=sending)
t2=threading.Thread(target=receive)
t1.start()
t2.start()
get_key()    
