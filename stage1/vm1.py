from scapy.all import *
print(Ether())
print(IP())
#sendp("hehe",iface="ens3",loop=1,inter=0.2)
p=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.10.2")
ans,_=srp(p,iface="ens3",timeout=10)
print(ans)
for s,r in ans:
        print(r[Ether].src)
