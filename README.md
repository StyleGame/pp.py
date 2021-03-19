import os, time
os.system('pip install --upgrade pip && pip install requests && pip install bs4')
os.system('clear')
import requests,json,random,string,termcolor,time,pyfiglet
from bs4 import BeautifulSoup
# -----------------------------------

logo='''
\033[1;34m______________
< StyleGame >
  ----------
    \
     \
                                   .::!!!!!!!:.
  .!!!!!:.                        .:!!!!!!!!!!!!
  ~~~~!!!!!!.                 .:!!!!!!!!!UWWW$$$
      :$$NWX!!:           .:!!!!!!XUWW$$$$$$$$$P
      $$$$$##WX!:      .<!!!!UW$$$$"  $$$$$$$$#
      $$$$$  $$$UX   :!!UW$$$$$$$$$   4$$$$$*
      ^$$$B  $$$$\     $$$$$$$$$$$$   d$$R"
        "*$bd$$$$       *$$$$$$$$$$$o+#"
             """"          """""""
   _____ _         _       _____
  / ____| |       | |     / ____|
 | (___ | |_ _   _| | ___| |  __  __ _ _ __ ___   ___
  \___ \| __| | | | |/ _ \ | |_ |/ _` |  _ ` _ \ / _ \
  ____) | |_| |_| | |  __/ |__| | (_| | | | | | |  __/
 |_____/ \__|\__, |_|\___|\_____|\__,_|_| |_| |_|\___|
              __/ |
             |___/
             
          \033[1;37m('follow my on tlegram @StyleGame1')
'''
print(logo)
print()
number = input("\x1b[0;35m Enter your number: ").strip()
print()
pwd = input("\x1b[0;33m Enter your password: ").strip()
print()
with requests.Session() as req:
    def generationLink(stringLingth):
        latters = string.ascii_lowercase
        return ''.join(random.choice(latters) for i in range(stringLingth))
    urlLoginPage = f'https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/auth?client_id=website&redirect_uri=https%3A%2F%2Fweb.vodafone.com.eg%2Far%2FKClogin&state=286d1217-db14-4846-86c1-9539beea01ed&response_mode=query&response_type=code&scope=openid&nonce={generationLink(10)}&kc_locale=en'
    responsePageLogin = req.get(urlLoginPage)
    soup = BeautifulSoup(responsePageLogin.content, 'html.parser')
    getUrlAction = soup.find('form').get('action')
    # print(getUrlAction)
    # ---------------------------------------------------
    headerRequest = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'web.vodafone.com.eg',
    'Origin': 'https://web.vodafone.com.eg',
    'Referer': urlLoginPage,
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
    }
    formData = {
    'username':number,
    'password':pwd
    }
    sendUserData = req.post(getUrlAction,headers=headerRequest,data=formData)
    checkRegistry = sendUserData.url
    _checkRegistry = checkRegistry.find('KClogin')
    # [2] Check the registry
    if _checkRegistry != -1:
        code = checkRegistry
        _code = code[code.index('code=') + 5:]
        headerAccessToken = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-GB,en;q=0.9,ar;q=0.8,ar-EG;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-type': 'application/x-www-form-urlencoded',
        'Host': 'web.vodafone.com.eg',
        'Origin': 'https://web.vodafone.com.eg',
        'Referer': 'https://web.vodafone.com.eg/ar/KClogin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
        }
        formDataAccessToken = {
        'code': _code,
        'grant_type': 'authorization_code',
        'client_id': 'website',
        'redirect_uri': 'https://web.vodafone.com.eg/ar/KClogin'
        }
        sendDataAccessToken = req.post('https://web.vodafone.com.eg/auth/realms/vf-realm/protocol/openid-connect/token',headers=headerAccessToken,data=formDataAccessToken)
jwt = sendDataAccessToken.json()['access_token']
url="https://mobile.vodafone.com.eg:443/mobile-app/promo/unifiedRedeemPromo"
headers={"Authorization": "Bearer "+(jwt)+"", "operatingSystem": "V11.0.8.0.PCOMIXM", "platform": "Android", "deviceType": "ginkgo", "buildNumber": "414",
"Content-Type": "application/json; charset=UTF-8", "Connection": "close", "Accept-Encoding": "gzip, deflate", "User-Agent": "okhttp/3.12.1"}
json={"channelId": 3, "contextualOperationId": 0, "contextualPromoId": 0, "operationId": 0, "param1": "Mama", "promoId": 3336, "triggerId": 332, "triggerType": "6", "wlistId": 3256}
r=requests.post(url, headers=headers, json=json)
g=r.json()['giftQuota']
print("")
if g == "200":
    print("تمت الاضافة بنجاح")
else:
	print("حاول غداا مره اخره")
