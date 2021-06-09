import requests,time
email=input('\033[1;92mEnter Your Email:')
ide=input('\033[1;92mEnter Your Id:')
nam=input('\033[1;92mEnter Your Name:')
token=input('\033[1;92mEnter Your Token:')
dev=input('\033[1;92mEnter Your Device Id:')
while True:
    hd={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.el-tarek.net"}
    url=('https://app.el-tarek.net/api/v1/register')
    data={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
    r=requests.post(url,headers=hd,data=data).json()
    check=r['message']
    print(check)
    print("\033[1;92m-"*50)
    c=r['data']
    m=c['api_token']
    hd2={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.el-tarek.net"}
    url2=("https://app.el-tarek.net/api/v1/unsubscribed-campaigns?api_token={}".format(m))
    data2={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
    r2=requests.get(url2,headers=hd2,data=data2).json()
    k=r2['data']
    Dark=k['id']
    hd3={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.el-tarek.net"}
    url3="https://app.el-tarek.net/api/v1/new-subscribe"
    data3={"api_token":m,"campaign_id":Dark}
    r3=requests.post(url3,headers=hd3,data=data3).json()
    watch=r3['message']
    print(watch)
    print("\033[1;92m-"*50)
    hd3={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8","User-Agent":"Mozilla/5.0 (Linux; Android 8.0.0; LDN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Mobile Safari/537.36","Host":"app.el-tarek.net"}
    url3=("https://app.el-tarek.net/api/v1/my-coins?api_token={}".format(m))
    data3={"email":email,"social_id":ide,"name":nam,"token":token,"type":"android","device_id":dev}
    r3=requests.get(url3,headers=hd3,data=data3).json()
    dog=r3['data']
    coin=dog['count_coins']
    print("Done Add Now You Have==>",coin)
    print("\033[1;92m-"*50)
