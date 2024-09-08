sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.bind(('',5005))

sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock2.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock2.bind(('',5006))

ip='20.198.19.177'


def receive():
       while True:  
             ck1, addr,mac = sock2.recvfrom(1024)
             print(f'The MAC ADDRESS of client with verified challange : {mac}')
                   
                    
def sending():
	while True:
		msg=input("message :  ")
		sock.sendto(msg, (ip, 5005))
		
		             
t1=threading.Thread(targe=sending)
t2=threading.Thread(target=receive)
t1.start()
t2.start()
get_key()    

