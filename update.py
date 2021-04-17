#/data/data/com.termux/files/usr/etc/apt
#termux-packages v2.0
#History : 14/1/2021
#By: Ahmed Mohamed (A 𝕝 - A 𝕝 𝕒 𝕞 𝕪) 
#Channel : https://www.youtube.com/channel/UCm-UlQ6ygk4jkNfgFzlc2LA
####################################################################
#deb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main
#deb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable
#deb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 stable
#deb https://mirrors.tuna.tsinghua.edu.cn/termux/unstable-packages unstable main
#deb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-root-packages-24 root main
#deb https://mirrors.tuna.tsinghua.edu.cn/termux/x11-packages x11 main
####################################################################
G="\033[0;32m" # Green
import os
os.system("clear")
os.system("clear")
#file1                                                                                                                
file = open('test.list','w')
myData = "deb https://termux.mentality.rip/termux-packages-24 stable main"
file.write(myData)
file.close()
os.system ("mv test.list sources.list")
os.system("cd sources.list.d")
#file2
file = open ('test2.list','w')
myData2 = "deb https://termux.mentality.rip/game-packages-24 games stable"
file.write(myData2)
file.close()
os.system ("mv test2.list game.list")
#file3
file = open ('test3.list','w')
myData3 = "deb https://termux.mentality.rip/science-packages-24 science stable"
file.write(myData3)
file.close()
os.system ("mv test3.list science.list")
#file4
file = open('test4.list','w')
myData4 = "deb https://termux.mentality.rip/unstable-packages unstable main"
file.write(myData4)
file.close()
os.system ("mv test4.list unstable.list")
#file5
file = open('test5.list','w')
myData5 = "deb https://termux.mentality.rip/termux-root-packages-24 root stable"
file.write(myData5)
file.close()
os.system ("mv test5.list root.list")
#file6
file = open('test6.list','w')
myData6 = "deb https://termux.mentality.rip/x11-packages x11 main"
file.write(myData6)
file.close()
os.system ("mv test6.list x11.list")
#file sources.list move (x)
#os.system ("mv sources.list sources.list.d") (x)
#file game.list move
os.system ("mv game.list sources.list.d")
#file science.list move
os.system ("mv science.list sources.list.d/")
#file unstable.list move
os.system ("mv unstable.list sources.list.d")
#file termux-root.list move
os.system ("mv root.list sources.list.d")
#file xll.list move 
os.system ("mv x11.list sources.list.d")
os.system("termux-open-url https://www.youtube.com/channel/UCm-UlQ6ygk4jkNfgFzlc2LA?sub_confirmation=1")
os.system("pkg update ; pkg upgrade")
os.system("clear")
print (G+"[+] Done..!")
