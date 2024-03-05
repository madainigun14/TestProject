import json
import requests
from lxml import etree


def page(total, amount):
    #Remainder quotient

    quotient, remainder = divmode(total, amount)
    
    print(quotient, remainder)


def get_words():
    _url_0="https://thai-notes.com/dictionaries/connectetym.php?count&langs='zh','yue','hak','ltc','cmn','nan','och','zhx-teo','ms'&types='bor','inh','der','cog'"
    _url_1="https://thai-notes.com/dictionaries/connectetym.php?filter&langs='zh','yue','hak','ltc','cmn','nan','och','zhx-teo','ms'&types='bor','inh','der','cog'&from=0"


    _request_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }
    with requests.request(method="GET", url=_url_1, headers=_request_headers)as response:
        print(response.text)
        print(response.readline())
        with open(file=r"c:\myscript\result.txt", mode="a", encoding="utf-8") as f:
            f.write(response.text)


    _url_2="https://thai-notes.com/dictionaries/connectetym.php?filter&langs='zh','yue','hak','ltc','cmn','nan','och','zhx-teo','ms'&types='bor','inh','der','cog'&from=" + str(number-1)

get_words()





