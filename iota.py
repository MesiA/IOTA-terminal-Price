
'''
Code with <3 from @ai_python by M.A.C.
If u want to have colored version use linux :)
'''

import urllib.request, json, time,os,platform, datetime
os_name = platform.system()
c = 'clear' if os_name.lower()== 'linux' else 'cls'
clear = lambda: os.system(c)

d = float(input('Enter Delay time in seconds:'))
d = 1 if d<1 else d

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
temp = 0
while 1:
    url = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/iota/")
    data = json.loads(url.read().decode())
    clear()
    print(bcolors.BOLD+bcolors.UNDERLINE+bcolors.OKBLUE+"\t\tIOTA PRICE Monitor"+bcolors.ENDC)
    color = bcolors.WARNING if temp > float(data[0]['price_usd']) else bcolors.OKGREEN
    temp = float(data[0]['price_usd'])
    print(
        '''  {4}Price (USD):{5}{7}{0}{5}
  {4}Change (1h):{5}{6}{1}%{5}
  {4}Change (1d):{5}{6}{2}%{5}
  {4}Change (1w):{5}{6}{3}%{5}
    '''.format(data[0]['price_usd'],data[0]['percent_change_1h'],data[0]['percent_change_24h'],data[0]['percent_change_7d'],bcolors.HEADER,bcolors.ENDC,bcolors.BOLD,color))
    print('Please join us at:{0} @ai_python{1}'.format(bcolors.OKGREEN,bcolors.ENDC))
    print('\tupdated at:',datetime.datetime.now())
    time.sleep(int(d))