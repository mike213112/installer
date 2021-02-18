#!/bin/bash

#echo 'export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_281' >> ~/.bashrc
#echo 'export PATH=JAVA_HOME/bin:$PATH' >> ~/.bashrc

#echo 'source ~/.bashrc'

# Commands
Update='sudo apt update; sudo apt upgrade -y'
Shh='sudo apt install openssh-client openssh-server -y'
Vim='sudo apt install vim -y'

# Files
Docker='requirements/docker.txt'
Java='requirements/java.txt'
DockerCompose='requirements/docker-compose.txt'
Nginx='requirements/nginx.txt'
Code='requirements/code.txt'
Sublime='requirements/sublime_text.txt'
Chrome='requirements/google_chrome.txt'
Brave='requirements/brave.txt'
Packet='requirements/packet_tracer.txt'
Oh='requirements/shell.txt'
Kubeamd='requirements/kubeadm.txt'
Teams='requirements/teams.txt'
Albert='requirements/albert.txt'
Flutter='requirements/flutter.txt'
Dart='requirements/dart.txt'
Android='requirements/android.txt'


# Links for Download 
LinkJava="https://mega.nz/file/Zbo0mD7C#gkI2ZhCiuZ7M35_fHw7MaL-gY-D8zzmtahHC8jMjD9w"
LinkCode="https://mega.nz/file/RaQRHISJ#3n-XI2R1u0kuVx_4sgcfX_P7auGWLUXd0HZZMPbZS2s"
LinkDatagrip="https://mega.nz/file/MCxVBQwa#uE8BZR8p2flymVw-sw4NePq2b5mX-wf8TClslB9epus"
LinkFlutter="https://mega.nz/file/FDxxVSyS#O2N3c7wX29w9xZm3XgZV3fvBAU64O_I-MFJTTAN3cQA"
LinkGoogle="https://mega.nz/file/lWhxHAQI#ISE69ZxJBuNxfW0BgPAzhwU14C60fkpm8qwfRfipAms"
LinkIdea="https://mega.nz/file/pP4jAAxJ#2nRD39hqXJZoZfVvxxTNLqv2Il0Yxbc-d59d7a4lxi0"
LinkNetbeas8="https://mega.nz/file/JegTRIRD#iWNq2X1wCr0Dh4PtBl-fpp4WjyzSI2JrMIYx4udWi08"
LinkJetbrains="https://mega.nz/file/gf4BACBb#VyPin5fqVF2jD-yYAq5hCgVZTtS4I1q8QeSqsa_ynQo"
LinkPacket="https://mega.nz/file/sL5nQaYI#mMO_h8BUuJlfKYkgkmipkdbpBj9V1b0JPcSAzS3rKIw"
LinkPhpstorm="https://mega.nz/file/0GpRCKgD#IeZ2oqVOltltIX1fcV7KpQiHtmQlPJ6miciR5btZwY8"
LinkPycharm="https://mega.nz/file/ZHxAAYJC#GhlqqTOp4-1Y-y0ZqnCHhdJBA7-FAKlzCr-p8gl7zPw"
LinkRuby="https://mega.nz/file/YSxESaYa#b5N7MVMgeNpa7jlLWnOuFAszMsORisk0QDpdUYXIXeM"
LinkTeams="https://mega.nz/file/RTpmgYhY#-dNXAQcLwiK40QNo60motp3ZXnrz0Vl5vYL3YIUpwP0"
LinkWebStorm="https://mega.nz/file/5WhglCzA#GH9Hbq8EL-qfhpbvcaKwOOPbd2p7iP9GkR_7VdkxYkc"
LinkAndroid="https://mega.nz/file/kCJVlIxT#nK5jYovhbD85On_JGHLPL8TvBbAIW8TdtMn0LwE8V5U"

UpdateAndUpgrade() {
    python3 -c "
    
from bin.funtions import UpdateAndUpgrade

system_update = UpdateAndUpgrade('$1')
system_update.update()

    "
}


InstallDocker() {
    python3 -c "

from bin.funtions import Docker

docker = Docker('$1')
docker.install_docker()

    "
}


InstallSsh() {
    python3 -c "
    
from bin.funtions import Shh

ssh = Ssh('$1')
ssh.install_ssh()
    "
}


InstallJava() {
    python3 -c "
    
from bin.funtions import Java

java = Java('$1','$2')
java.install_java()

    "
}


InstallDockerCompose() {
    python3 -c"
    
from bin.funtions import DockerCompose

compose = DockerCompose('$1')
compose.install_docker-compose()

    "
}


InstallNginx() {
    python3 -c "
    
from bin.funtions import Nginx

nginx = Nginx('$1')
nginx.install_nginx()

    "
}


InstallVim() {
    python3 -c "
    
from bin.funtions import Vim

vim = Vim('$1')
vim.install_vim()

    "
}


InstallVisualStudioCode() {
    python3 -c "
    
from bin.funtions import VisualStudioCode

code = VisualStudioCode('$1','$2')
code.install_visual_studio_code()
    
    "
}


InstallSublimeText() {
    python3 -c "
    
from bin.funtions import SublimeText

sublime = SublimeText('$1')
sublime.install_sublime_text_3()

    "
}


InstallGoogleChrome() {
    python3 -c "
    
from bin.funtions import GoogleChrome

chrome = GoogleChrome('$1','$2')
chrome.install_google_chrome()

    "
}


InstallBraveBrowser() {
    python3 -c "
    
from bin.funtions import Brave

brave = Brave('$1')
brave.install_brave()
    
    "
}


CustomizeTerminal() {
    python3 -c "
    
from bin.funtions import Terminal

terminal = Terminal('$1')
terminal.customize_terminal()
    
    "
}


InstallPacketTracer() {
    python3 -c "
    
from bin.funtions import PacketTracer

packet = PacketTracer('$1','$2')
packet.install_packet_tracer()
    
    "
}


InstallKubeamd() {
    python3 -c "
    
from bin.funtions import Kubeamd

kubeadm = Kubeamd('$1')
kubeadm.install_kubeamd()

    "
}


InstallPycharm() {
    python3 -c "
    
from bin.funtions import Pycharm

pycharm = Pycharm('$1','$2')
pycharm.install_pycharm()
    
    "
}


InstallIdea() {
    python3 -c "
    
from bin.funtions import Idea

idea = Idea('$1','$2')
idea.install_intellij_idea()
    
    "
}


InstallDatagrip() {
    python3 -c "
    
from bin.funtions import Datagrip

datagrip = Datagrip('$1','$2')
datagrip.install_datagrip()
    
    "
}


InstallNetbeans8() {
    python3 -c "
    
from bin.funtions import Netbeans8

netbeans = Netbeans8('$1','$2')
netbeans.install_netbeans_8_2()

    "
}


InstallNetbeans12() {
    python3 -c "
    
from bin.funtions import Netbeans12

netbeans = Netbeans12('$1','$2')
netbeans.install_netbeans_12()
    
    "
}


InstallRider() {
    python3 -c "
    
from bin.funtions import Rider

rider = Rider('$1','$2')
rider.install_intellij_rider()
    
    "
}


InstallPhpStorm() {
    python3 -c "
    
from bin.funtions import PhpStorm

php = PhpStorm('$1','$2')
php.install_intellij_phpstorm()
    
    "
}


InstallRuby() {
    python3 -c "
    
from bin.funtions import Ruby

ruby = Ruby('$1','$2')
ruby.install_intellij_ruby()
    
    "
}


InstallTeams() {
    python3 -c "
    
from bin.funtions import Teams

teams = Teams('$1','$2')
teams.install_teams()
    
    "
}


InstallWebStorm() {
    python3 -c "
    
from bin.funtions import WebStorm

web = WebStorm('$1','$2')
web.install_intellij_webstorm()
    
    "
}


InstallFlutter() {
    python3 -c "  

from bin.funtions import Flutter

flutter = Flutter('$1','$2')
flutter.install_flutter()

    "
}


InstallAndroidStudio() {
    python3 -c " 

from bin.funtions import AndroidStudio

android = AndroidStudio('$1','$2')
android.install_android_studio()

    "
}


InstallAlbert() {
    python3 -c "
    
from bin.funtions import Albert

albert = Albert('$1')
albert.install_albert_for_ubuntu_20_04()
    
    "
}


while : 
do
    echo "Menu de opciones
0. Salir.
1. Actualizar el sistema.
2. Instalar docker.
3. Instalar ssh.
4. Instalar java. 
5. Instalar docker-compose. 
6. Instalar nginx. 
7. Instalar vim. 
8. Instalar Visual Studio Code. 
9. Instalar Sublime Text 3. 
10. Instalar Google Chrome. 
11. Instalar Brave Brower. 
12. Instalar Packet Tracer. 
13. Instalar Oh my bash. 
14. Instalar Kubeadm. 
15. Instalar Teams.
16. Instalar Albert para ubuntu 20.04. 
17. Instalar Flutter.
18. Instalar Dart. 
19. Instalar Android Studio."
    read opcion
    
    if [ $opcion = 0 ]; then
        exit 0
    elif [ $opcion = 1 ]; then
        UpdateAndUpgrade $Update
        echo ''
    elif [ $opcion = 2 ]; then
        InstallDocker $Docker
        echo ''
    elif [ $opcion = 3 ]; then 
        InstallSsh $Ssh
        echo ''
    elif [ $opcion = 4 ]; then
        InstallJava $LinkJava $Java
        echo ''
    elif [ $opcion = 5 ]; then
        InstallDockerCompose $DockerCompose
        echo ''
    elif [ $opcion = 6 ]; then
        InstallNginx $Nginx
        echo ''
    elif [ $opcion = 7 ]; then
        InstallVim $Vim
        echo ''
    elif [ $opcion = 8 ]; then
        InstallVisualStudioCode $LinkCode $Code 
        echo ''
    elif [ $opcion = 9 ]; then
        InstallSublimeText $Sublime
        echo ''
    elif [ $opcion = 10 ]; then
        InstallGoogleChrome $LinkGoogle $Chrome
        echo ''
    elif [ $opcion = 11 ]; then
        InstallBraveBrowser $Brave
        echo ''
    elif [ $opcion = 12 ]; then
        InstallPacketTracer $LinkPacket $Packet
        echo ''
    elif [ $opcion = 13 ]; then
        CustomizeTerminal $Oh 
        echo ''
    elif [ $opcion = 14 ]; then
        InstallKubeamd $Kubeamd
        echo ''
    elif [ $opcion = 15 ]; then
        InstallTeams $LinkTeams $Teams
        echo ''
    elif [ $opcion = 16 ]; then
        InstallAlbert $Albert
        echo ''
    elif [ $opcion = 17 ]; then
        InstallFlutter $LinkFlutter $Flutter
        echo ''
    elif [ $opcion = 18 ]; then
        InstallAndroidStudio $LinkAndroid $Android
        echo ''
    fi

done
