# Simple-Python-Trojan
A simple python trojan for 3.8 that creates a backdoor via netcat. 

## Usage
Using the script varies from OS to OS.

The reverse shell currently connects to a netcat listener at 192.168.100.153 on port 9501.  
To change the IP/port:
1) Edit the IP and port in shell.py
2) Encode shell.py to base64
3) Copy and paste the encoded string into decoder.py
4) (optional) Compile decrypt.py with pyinstaller

###  Windows
Windows is a bit more tricky because it doesn't ship with python.  To work around 
this, the script is configured to run an embeddable python interpreter to do all the work.  
It's available at: https://www.python.org/ftp/python/3.9.0/python-3.9.0-embed-amd64.zip

From here, it's just a matter of running decoder.exe on the victim machine. 

### Linux
This trojan is developed for Windows, but thanks to how universal python is, it will run on most any operating system.
To change the target OS to Linux, simply change the `check_output` command on line 20 to `python3 Output.py`.

### MacOS
Compatability is unknown.  I believe you could build it to some sort of executable or have a script to run it, but I have not tested it personally.  


## Disclaimer
Please use this program in a legal manner.  I am not responsible for any damages caused by this software.  
