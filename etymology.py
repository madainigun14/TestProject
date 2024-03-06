# https://thai-notes.com/dictionaries/etymdict.html 
# 泰国国家电子和计算机技术中心NECTEC(National Electronics and Computer Technology Center)

import re
import requests

langs_all = "'thm','aho','aio','ami','ar','arc','aav','bn','pcc','qfa-onb-pro','my','ca','ceb','cjm','cja','zh','yue','hak','ltc','cmn','nan','och','zhx-teo','cog','da','dv','kmc','nl','dum','dz','en','fr','fro','lg','de','el','grc','gu','xhm','nan-hai','haw','he','hil','hi','lic','nan-hok','id','iu','tts','it','ium','ja','jv','kar','ckv','kaw','kht','kha','km','kxm','okz','okz-P','okz-A','kkh','ko','uun','kdt','lbc','lo','lwl','lcp','la','onb','khb','mg','ms','mfa','ml','mi','mr','meo','mkh-mmn','mnw','mkh','mul','mtq','ne','zhn','nut','cbn','nyw','gmq-oda','omx','obr','ota','pwn','pau','pi','fa','phk','pt','pra','map-pro','dra-pro','qfa-lic-pro','hmx-pro','inc-pro','ine-pro','iir-pro','qfa-kms-pro','mkh-khm-pro','poz-mly-pro','poz-mcm-pro','poz-pro','poz-msa-pro','mkh-pro','sit-pro','tai-swe-pro','tai-pro','mkh-vie-pro','pim','raj','ru','skb','sa','sh','shn','si','fos','es','swi','su','sw','tl','blt','tyj','twh','tdd','ta','tyz','tai-shz','te','th','nod','sou','ssf','bo','txb','tr','ur','sa-ved','vi','yno','za','zzj'"
langs_mainstream = "'ar','my','zh','yue','hak','ltc','cmn','nan','och','zhx-teo','cog','kmc','en','fr','fro','de','el','hi','id','ja','km','kxm','okz','okz-P','okz-A','ko','ms','pi','mkh-khm-pro','mkh-vie-pro','sa','es','blt','tyj','twh','tdd','th','nod','sou','bo','vi','za','zzj'"
langs_chinese = "'zh','yue','hak','ltc','cmn','nan','och','zhx-teo'"
langs = langs_mainstream
types = "'bor','inh','der','cog'"  # 词汇类型：借用、继承、派生、同源

def page(total, amount):
    """
    total=627       总数据
    amount=100      每页数据
    quotient=6      分页的数量
    remainder=27    最后一页的条目数
    """
    quotient, remainder = divmod(total, amount)
   
    print(quotient, remainder)


def get_words():
    """
    注意，后边的条件 
    第一页 from=0
    第二页 from=100
    第三页 from=200
    第四页 from=300
    第五页 from=400
    第六页 from=500
    第七页 from=600
    实际有627条数据
    """
    
    _from = 0  # 分页后，数据的起始值 0
    _url_0="https://thai-notes.com/dictionaries/connectetym.php?count&langs='zh','yue','hak','ltc','cmn','nan','och','zhx-teo','ms'&types='bor','inh','der','cog'"  # 无法获得想要的数据
    _url_1="https://thai-notes.com/dictionaries/connectetym.php?filter&langs=" + langs + "&types=" + types + "&from=" + str(_from)

    
    # 请求头，自己编一个
    _request_headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "close",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }
    with requests.request(method="GET", url=_url_1, headers=_request_headers)as response:
        #print(response.text)
        line1 = response.text.split("\n")[0]
        total = int("".join(re.findall(r"\d+", line1)))  # 求出，该langs+types下，总共有多少条数据
        print(total) 
        try:
            with requests.request(method="GET", url=_url_1, headers=_request_headers)as response:
                with open(file=r"c:\myscript\result.txt", mode="a+", encoding="utf-8") as f:
                    f.write(response.text)
        except Exception as e:
            print(e)        
    
    q, r = divmod(total, 100)  # 求出分页的页码数q，和最后一页有多少条数据r
    
    for i in range(q):
        """
        遍历q次分页，把返回值添加的文本文件里
        """
        _url_2 = "https://thai-notes.com/dictionaries/connectetym.php?filter&langs=" + langs + "&types=" + types + "&from=" + str(100*(i+1))
        print(_url_2)
        try:
            with requests.request(method="GET", url=_url_2, headers=_request_headers)as response:
                with open(file=r"c:\myscript\result.txt", mode="a+", encoding="utf-8") as f:
                    text_without_line1 = "\n".join(response.text.split("\n")[1:])
                    f.write(text_without_line1)
        except Exception as e:
            print(e)
        
    
get_words()
