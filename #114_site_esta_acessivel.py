# Crie um código em Python que teste se o site Pudim está acessível pelo computador usado.

import requests
import urllib.request

try:
    # site = requests.get('http://www.pudim.com.br')
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim NÃO está no ar')
else:
    print('O site Pudim está no ar')
    # print(site.read())



# siteReturn = site.status_code

# if siteReturn == 200:
    
# else:
    