from scapy.all import *;
p=Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst="192.168.10.1")
ans,_=srp(p,iface="ens3",timeout=10)
print(ans)
for s,r in ans:
        print(r[Ether].src)
