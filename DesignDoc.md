# Ethical Hacking Tools #  


### Hacker 5: Abdullah Sairafi, Aziz Nassar, Jasmine Rattan, Matthew Scates, Obaid Hasseeb ###
#### 06/09/2020 ####

## INTRODUCTION ##
Explain the problem:  
Many people use public networks in various places which are notoriously known for unsecured WIFI networks.  
These networks can be compromised, making it easy for the malicious users to steal user’s data without the user’s permission.   
As a result, users are susceptible to SSH and FTP attacks, ARP spoofing, and reverse shell attacks.   
This problem is important because people can get private information leaked and stolen. Also, many people are not  
aware of how damaging the public WIFI connection could be to the user’s sensitive information. Therefore, we decided   
to utilize tools such as Reverse shell, Arp spoofer, ssh and ftp attacks, and keylogger to show what kind of data can  
be leaked.  


#### Our findings: ####
Our findings from the reverse shell: We found that if the attacker can control the target computer,   
the attacker can operate various operations such as uploading, downloading, browsing the file system of the attacked user.   
This is done via socket programming where the attacker maintains a backdoor to the target system,   
making the user connect to the attacker’s server whenever they run the attacker’s shell.?  

Our findings from SSH and FTP attacks: We found that once you have access to a users account, 
you get control of their entire terminal which is pretty fascinating and scary. A Conjunctoin of our tools  
can really get a lot of information from somebody.  

Our findings from ARP Spoofer: We have found that when using the arp command in the terminal,      
my mac address is shown twice when using the ARP command, one from a dynamic IP address and     
one from a static IP address. This indicates that my mac IP address is under a different IP     
address from before indicating a It does take multiple tries to see the change with the “arp -a” command.    
Our findings from Keylogger:   

Our findings from Keylogger: We found that the attacker is able to read and monitor every keystroke the target machine is writing in their system. We used Kali Linux as our target machine and Ubuntu machine as our attacking machine. We used pynput.keyboard library to record the keystrokes the user is typing. 

### SKETCH OF REVERSE SHELL  ###

<img src = "https://scontent-sjc3-1.xx.fbcdn.net/v/t1.15752-9/102394859_575458426706668_5572030561150967953_n.jpg?_nc_cat=104&_nc_sid=b96e70&_nc_ohc=F2f5ZHcc9H8AX-WekMd&_nc_ht=scontent-sjc3-1.xx&oh=42a9af5beb016a4e0846a51231dda5f8&oe=5F03F42B" width="200"/>

### EXPLAIN THE SKETCH  ###

So the attacker will see a nice advertisement that claims to offer free stuff.   
But once the target goes to this fishy site, the attacker can take over the user and perform  
various operations such as uploading and downloading files, and browsing the file system of the user,   
meanwhile the user is unaware of this happening.   


