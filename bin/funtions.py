import os
import time
from getpass import getuser
from mega import Mega
# from progress.spinner import Spinner


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
        M.download_url(self.url)

        file = open(self.files,'r')
        dato = file.read()
        datos = dato.split(';')

        for i in datos:
            os.system(i)


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
                os.system(i)
                move = '/home/' + USER
            os.system(i)


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