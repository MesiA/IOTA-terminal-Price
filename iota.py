
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

bcolors = {
    'header_c' : '\033[95m'
    'okblue_c' : '\033[94m'
    'okgreen_c' : '\033[92m'
    'warning_c' : '\033[93m'
    'fail_c' : '\033[91m'
    'end_c' : '\033[0m'
    'bold_c' : '\033[1m'
    'underline_c' : '\033[4m'
}
temp = 0
while 1:
    url = urllib.request.urlopen("https://api.coinmarketcap.com/v1/ticker/iota/")
    data = json.loads(url.read().decode())
    clear()
    print("{bold_c}{underline_c}{okblue_c}\t\tIOTA PRICE Monitor{end_c}".format(**bcolors))
    color = bcolors['warning+c'] if temp > float(data[0]['price_usd']) else bcolors['okgreen_c']
    temp = float(data[0]['price_usd'])
    print(
        '''  {header_c}Price (USD):{end_c}{color}{price_usd}{end_c}
  {bold_c}Change (1h):{end_c}{bold_c}{price_change_1h}%{end_c}
  {bold_c}Change (1d):{end_c}{bold_c}{percent_change_24h}%{end_c}
  {bold_c}Change (1w):{end_c}{bold_c}{percent_change_7d}%{end_c}
    '''.format(**data[0], **bcolors))
    print('Please join us at:{okgreen_c} @ai_python{end_c}'.format(**bcolors))
    print('\tlast updated at:',datetime.datetime.now())
    time.sleep(int(d))
