import socket

s=socket.socket()
s2=socket.socket()
port=4004
ip='20.198.19.177'
port2=5005
s2.bind('',port2)
def receive():
       while True:  
             s.connect((ip,port))
             msg=s.recv(1024).decode())
             print(msg)
             
                    
def sending():
	while True:
    c,addr=s2.accept()
		msg=input("message :  ")
		c.send(msg)
		
		             
t1=threading.Thread(targe=sending)
t2=threading.Thread(target=receive)
t1.start()
t2.start()
get_key()    
