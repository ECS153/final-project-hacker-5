# Hacker5
Authors: Abdullah, Aziz, Jasmine, Matthew, Obaid

## What does our project do?
  We created tools such as Reverse shell, Keylogger, Arp spoofer, SSH and FTP Attacks to show what could happen if you download software from malicious websites and how public connections could steal your private information. We show the vulnerabilities of computer system. 

## Setting up and Running our Code
  Since there are four different tools we utilized, each of them have different steps of setting up and running. We will show you the steps of each of the tools we created, starting with keylogger.
  
### How to set up and run keylogger:
  Getting started with Keylogger(tools you need to download):
    1. To be able to run the keylogger, you need to install pynput library: pip install pynput
    2. f you are using python3, you might need pip3 install pynput
    3. Then, type python in the terminal. Once you are in the command line, type the following: import pynput.keyboard, followed by exit()
    4. Finally, install the keyboard library: pip install pynput.keyboard (if you are on python3, you might need pip3)
    
   How to run the keylogger:
   Note: While running the keylogger, we worked with two different machines, one Ubuntu(attacker) and another kali linux      VM(target). Follow the steps below to run the keylogger:
Also, you must change the IP Address in shell.py and server.py  to your own IP Address. Currently, it is a hard coded value. It would be at line 

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

