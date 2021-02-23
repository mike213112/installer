import os
import time
from getpass import getuser
from mega import Mega
from progress.spinner import Spinner
import glob
import sys


USER = getuser()
mega = Mega()
M = mega.login()


class Docker:
    def __init__(self,files):
        self.files = files


    def install_docker(self):
        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            if i == 'sudo docker -aG docker':
                add_docker = i + ' ' + USER
                os.system(add_docker)
            else:
                os.system(i)


class Ssh:
    def __init__(self,command):
        self.command = command


    def install_ssh(self):
        os.system(self.command)


class Java:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_java(self):
        file = r'*.gz'
        listar = glob.glob(file)
        # print(listar)

        new_file = ''
        name_file = ''
        pwd = os.getcwd()

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            if 'sudo apt install' in i:
                os.system(i)
            if 'tar -xzvf' in i:
                for x in listar:
                    descomprimir = i + ' ' + x
                    # print(listar)
                    os.system(descomprimir)
                    new_file = descomprimir
                    name_file = x
            if 'sudo rm -r' in i:
                # listar_archivos = os.listdir()
                # if listar in listar_archivos:
                for y in listar:
                    os.remove(y)
            if 'sudo mv' in i:
                for files in os.listdir():
                    if 'jdk1' in files:
                        mover = i + " " + files + " /usr/bin/jvm"
                        os.system(mover)
                        # print(mover)
                        

class DockerCompose:
    def __init__(self,files):
        self.files = files


    def install_docker_compose(self):
        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class Nginx:
    def __init__(self,files):
        self.files = files


    def install_nginx(self):
        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class NginxIpMaster:
    def __init__(self,ip1,ip2,files):
        self.ip1 = ip1
        self.ip2 = ip2
        self.files = files


    def configure_ip(self):
        file = open(self.files,'a')
        line_1 = '\n\t\tserver {}:6443;$'.format(self.ip1)
        line_2 = '\n\t\tserver {}:6443;$'.format(self.ip2)

        file.write(line_1)
        file.write(line_2)

        restante = ['\n\t}$','\n\tserver {$','\n\t\tlisten 6443;$','\n\t\tlisten 443;$','\n\t\tproxy_pass kubernetes;$','\n\t}$','\n}$','\nEOF$']

        for i in restante:
            file.write(i)

        file.close()

        file2 = open('requirements/Nginx/masterip.txt','r')
        data = file2.read()
        datas = data.split('$')

        varia = ''
        for x in datas:
            varia += x
        
        print(varia)
        # os.system(varia)


class Vim:
    def __init__(self,command):
        self.command = command


    def install_vim(self):
        os.system(self.command)


class VisualStudioCode:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_visual_studio_code(self):
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class SublimeText:
    def __init__(self,files):
        self.files = files


    def install_sublime_text_3(self):        
        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class GoogleChrome:
    def __init__(self,url,files):
        self.url = url
        self.files = files

    def install_google_chrome(self):        
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class Brave:
    def __init__(self,files):
        self.files = files


    def install_brave(self):
        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class Terminal:
    def __init__(self,files):
        self.files = files


    def customize_terminal(self):
        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class PacketTracer:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_packet_tracer(self):
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class Pycharm:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_pycharm(self):        
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)

        dir = '/home' + USER
        move = '' 
        archivo = ''

        listar = os.listdir(dir)

        for i in listar:
            if 'Descargas' in i or 'Downloads' in i:
                dir += '/' + i 

        dir_new = os.listdir()

        for i in dir_new:
             if 'pycha' in i or 'Pycha' in i:
                move += 'mv ' + i + dir
                archivo += i
                os.system(move)

        dir_new2 = dir + archivo
        run = 'sh ' + dir_new2 + 'pycharm.sh'
        os.system(run)


class Idea:
    def __init__(self,url,files):
        self.url = files
        self.files


    def install_intellij_idea(self):        
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class Datagrip:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_datagrip(self):        
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            if 'datagrip' in datos:
                # os.system(i)
                move = '/home/' + USER
                print(move)
            # os.systFem(i)


class Netbeans8:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_netbeans_8_2(self):        
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class Netbeans12:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_netbeans_12(self):        
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class Rider:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_intellij_rider(self):        
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class PhpStorm:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_intellij_phpstorm(self):        
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class Ruby:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_intellij_ruby(self):        
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class Teams:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_teams(self):        
        M.download_url(self.url)

        file = open(self.files)
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class WebStorm:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_intellij_webstorm(self):
        
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class Albert:
    def __init__(self,files):
        self.files = files


    def install_albert_for_ubuntu_20_04(self):
        #M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class UpdateAndUpgrade:
    def __init__(self,command):
        self.command = command


    def update(self):
        os.system(self.command)


class Kubeamd:
    def __init__(self,files):
        self.files = files


    def install_kubeamd(self):
        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class Flutter:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_flutter(self):
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class Dart:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_dart(self):
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


class AndroidStudio:
    def __init__(self,url,files):
        self.url = url
        self.files = files


    def install_android_studio(self):
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)

class Nvm:
    def __init__(self,files):
        self.files = files

    
    def install_nvm(self):
        file = open(self.files,'r')
        dato = file.read()

        command = ''

        for i in dato.split(';'):
            command += i

        os.system(command)


class Angular:
    def __init__(self,files):
        self.file = files


    def install_angular(self):
        file = open(self.files,'r'):
        dato = file.read()

        for i in dato.split(';'):
            os.system(i)


class Vue:
    def __init__(self,files):
        self.files = files

    
    def install_vue(self):
        file = open(self.files,'r'):
        dato = file.read()

        for i in dato.split(';'):
            os.system(i)