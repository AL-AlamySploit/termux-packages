#cd ~/../usr/etc/apt/; echo deb https://termux.mentality.rip/termux-packages-24 stable main>sources.list;cd sources.list.d;echo deb https://termux.mentality.rip/science-packages-24 science stable>science.list;echo deb https://termux.mentality.rip/game-packages-24 games stable>game.list;echo deb https://termux.mentality.rip/unstable-packages unstable main>unstable.list;cd ~; clear; apt update ; apt upgrade
A='\033[01;32m'
cd ~/../usr/etc/apt/; echo deb https://mirrors.tuna.tsinghua.edu.cn/termux/termux-packages-24 stable main>sources.list;cd sources.list.d;echo deb https://mirrors.tuna.tsinghua.edu.cn/termux/science-packages-24 science stable>science.list;echo deb https://mirrors.tuna.tsinghua.edu.cn/termux/game-packages-24 games stable>game.list;echo deb https://mirrors.tuna.tsinghua.edu.cn/termux/unstable-packages unstable main>unstable.list;cd ~; clear; apt update ; apt upgrade
echo "$A[+] Done..!"
