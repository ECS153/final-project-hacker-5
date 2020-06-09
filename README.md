# Hacker5
Authors: Abdullah, Aziz, Jasmine, Matthew, Obaid

## What does our project do?
  We created tools such as Reverse shell, Keylogger, ARP spoofer, SSH and FTP Attacks to show what could happen if you download software from malicious websites and how public connections could steal your private information. We show the vulnerabilities of computer systems inside the same network with our code, and found that we can get control over other users’ computers and retrieve sensitive information with various methods.

## Setting up and Running our Code
  Since there are four different tools we utilized, each of them have different steps of setting up and running. We will show you the steps of each of the tools we created, starting with keylogger.
  
### How to set up and run keylogger:
  #### Getting started with Keylogger(tools you need to download):
  1. To be able to run the keylogger, you need to install pynput library: pip install pynput
  2. f you are using python3, you might need pip3 install pynput
  3. Then, type python in the terminal. Once you are in the command line, type the following: import pynput.keyboard, followed by exit()
  4. Finally, install the keyboard library: pip install pynput.keyboard (if you are on python3, you might need pip3)
    
   #### How to run the keylogger:
   ##### Note: While running the keylogger, we worked with two different machines, one Ubuntu(attacker) and another kali linux      VM(target). Follow the steps below to run the keylogger:
   #### Also, you must change the IP Address in shell.py and server.py  to your own IP Address. Currently, it is a hard coded value. It would be at line 106 in shell.py and line 65 in server.py

1. (On terminal/ubuntu terminal)We first create the executable file for the shell. We used python package called pyinstaller to create an executable file for the shell to do this: python -m PyInstaller shell.py
 1.1 This will create a dist directory 
2. On another tab of the terminal, we run the server. To run the server: python server.py
3. While the server is running, we copy the dist directory that the executable created to the kali linux machine. You can copy it anywhere. We copied it on the desktop.
4. On the target computer(which is kali linux), do the following: #both these commands are basically the target running our shell
4.1 cd dist/shell                     
4.2 comiple: ./shell     ##make sure the server is running on your another machine terminal
5. Then, go to ubuntu terminal, and type keylog_start. This will start the process of reading anything you type in kali linux terminal
6. Go to the target machine(kali linux in our case), write any sentence. For instance, “Hello, this is Jasmine”
7. Then go back to the server(Ubuntu terminal), and type keylog_dump. This will dump out “Hello, this is Jasmine”
8. You can also see it create a text file called “keylogger.txt” on the ubuntu machine(attacker) which contains the contents of what you wrote in Kali linux machine(target)

### Next, we will discuss how to run reverse shell:
1. On your target machine, run the server. To run the server: python server.py
2. To run the shell: We used python package called pyinstaller to create an executable file for the shell to do this: python -m PyInstaller shell.py
 2.1 This will create a dist directory 
3. Now copy the dist directory to the target computer
4. On the target computer, do the following: #both these commands are basically the target running our shell
4.1 cd dist/shell                     
4.2 comiple: ./shell  


### How to set up and run SSH Attacks:
1) On Kali linux, go on root 
Type “su -p” and follow all of the commands in root
 2) Download the pexpect module.
pip install pexpect
pip3 inatall pexpect
pip install term color
	3) Run the programs 
Run the programs by typing “python sshlogin.py” and “python brutessh.py”
-> Then run the program with the following commands:
1. python sshlogin.py 
2. Type in the ip address, username and password


### How to set up and run ARP Spoofer:
1. First you need to download the scapy module, using this command on the terminal: 
    1.1 pip install scapy
2. Or download it off github here: https://github.com/secdev/scapy
3. Next, you will have a scapy folder, inside that scapy folder is where you place the arpSpoofer.py
4. To run it, go to the scapy directory inside the terminal and use ./arpSpoofer.py, then let the program run. 
5. Next, if you have another device or virtual machine, run “arp -a” on this other machine and you should see under one of the dynamic IP addresses the MAC address will be different.

## File Structure
All our code files are located in final-project-hacker-5/src
1. shell.py:
 This file is the backdoor to the target system
2. server.py
 It is the connection point to the target system. Server and shell are connected through a tcp socket. 
2. ARPSpoofer.py
 This is to perform man-in-the-middle attack. The spoof is performed by just running the code, you will need the scapy module.
3. Anonloginftp.py, brutessh.py, and sshlogin.py
	-this is for SSH and FTP attacks. 
5. keylogger.py
 Keylogger tracks and records every key that was inputted by the target. 
7. ports_scanner.py
This file checks the vulnerable ports open on a target machine.
