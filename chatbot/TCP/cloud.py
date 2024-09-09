import socket

s1=socket.socket()
s1.bind(('',4004))
s1.listen(5)
s2=socket.socket()
s2.bind(('',5005))
s2.listen(5)
c1,addr1=s1.accept()
c2,addr2=s2.accept()

port1=4004
port2=5005
ip='20.198.19.177'

def A():
       while True:
		
		x=c1.recv(1024))
		c2.send(x)		    
                    
def B():
	while True:
		
		x=c2.recv(1024))
		c1.send(x)	
		             
t1=threading.Thread(target=A)
t2=threading.Thread(target=B)
t1.start()
t2.start()
   
