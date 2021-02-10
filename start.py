#/data/data/com.termux/files/usr/etc/apt
#termux-packages v1.0
#History : 14/1/2021
#By:Ahmed Mohamed (A l - A l a m y) 
import os
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
#sources.list move (x)
#os.system ("mv sources.list sources.list.d") (x)
#game.list move
os.system ("mv game.list sources.list.d")
#science.list move
os.system ("mv science.list sources.list.d/")
#unstable.list move
os.system ("mv unstable.list sources.list.d")
os.system("clear")
os.system("pkg update ; pkg upgrade")
os.system("clear")
print ("Done..")
