#!/bin/bash

#Modified install.sh

printf '\033]2;install.sh\a'

G="\033[1;34m[*] \033[0m"
S="\033[1;32m[+] \033[0m"
E="\033[1;31m[-] \033[0m"
if [[ $(id -u) != 0 ]]; then
    echo -e ""$E"Permission denied!"
    exit
fi

{
    CHECK="$(ping -c 1 -q www.google.com >&/dev/null; echo $?)"
} &> /dev/null

if [[ "$CHECK" != 0 ]]; then 
    echo -e ""$E"No Internet connection!"
    exit
fi

sleep 0.5
clear
sleep 0.5
cat banner/banner.txt
echo

sleep 1
echo -e ""$G"Installing dependencies... (can take 5 minutes)"
sleep 1

{
    pkg update
    pkg -y install git
    pkg -y install python
    pkg -y install android-tools
    pkg -y install scrcpy
    pkg -y python3-pip
    apt-get update
    apt-get -y install git
    apt-get -y install python3
    apt-get -y install adb
    apt-get -y install scrcpy
    apt-get -y python3-pip
    apk update
    apk add git
    apk add python3
    apk add android-tools
    apk add scrcpy
    apk add python3-pip
    pacman -Sy
    pacman -S --noconfirm git
    pacman -S --noconfirm python3
    pacman -S --noconfirm android-tools
    pacman -S --noconfirm scrcpy
    pacman -S --noconfirm python3-pip
    zypper refresh
    zypper install -y git
    zypper install -y python3
    zypper install -y android-tools
    zypper install -y scrcpy
    zypper install -y python3-pip
    yum -y install git
    yum -y install python3
    yum -y install android-tools
    yum -y install scrcpy
    yum -y install python3-pip
    dnf -y install git
    dnf -y install python3
    dnf -y install android-tools
    dnf -y install scrcpy
    dnf -y install python3-pip
    eopkg update-repo
    eopkg -y install git
    eopkg -y install python3
    eopkg -y install android-tools
    eopkg -y install scrcpy
    eopkg -y install python3-pip
    xbps-install -S
    xbps-install -y git
    xbps-install -y python3
    xbps-install -y android-tools
    xbps-install -y scrcpy
    pip3 install -r $(pwd)/requirements.txt

} &> /dev/null


if [[ -d ~/ghost ]]; then
    cd ~/ghost
else
    echo -e ""$E"Installation failed!"
    exit
fi
