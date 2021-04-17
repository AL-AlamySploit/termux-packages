#/data/data/com.termux/files/usr/etc/apt
#termux-packages v1.0
#History : 14/1/2021
#By: Ahmed Mohamed (A l - A l a m y) 
#Channel : https://www.youtube.com/channel/UCm-UlQ6ygk4jkNfgFzlc2LA
import os
os.system("clear")
os.system("mv update.py /data/data/com.termux/files/usr/etc/apt")
os.system("cd /data/data/com.termux/files/usr/etc/apt")
os.system("pkg install python")
os.system("python update.py")
