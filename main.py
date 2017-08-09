#-*-coding:utf8;-*-
#qpy:2
#qpy:console
# -*- coding: utf-8 -*-
import re
import sys
import requests
import time
#sys.setdefaultencoding('utf-8')
requests.packages.urllib3.disable_warnings()
HEADER = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8',
          }

########################################################

def validUsefulProxy(proxy,url):
	    """
	    检验代理可以性
	    :param proxy:
	    :return:
	    """
	    proxies = {"http": "http://{proxy}".format(proxy=proxy),
	               "https": "https://{proxy}".format(proxy=proxy)}
	    try:
	        r = requests.get(url, proxies=proxies, timeout=2, verify=False)
	        if r.status_code == 200:
	            return True
	    except Exception, e:
	        return False

###########################################################


def freeProxySecond(proxy_number=10):
    #url = "http://www.66ip.cn/mo.php?sxb=&tqsl={}&port=80".format(proxy_number)
    url="http://www.66ip.cn/mo.php?sxb=&tqsl={}&port=80&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=".format(proxy_number)
    html = requests.get(url, headers=HEADER).content
    for proxy in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', html):
        proxy_handle(proxy)


###########################################################

def proxy_handle(proxy):
    #print proxy
    #print "HTTP:" + str(validUsefulProxy(proxy, 'http://m.so.com/'))
    #print "HTTPS:" + str(validUsefulProxy(proxy, 'https://m.so.com/'))
    # yield proxy
    http_bool=validUsefulProxy(proxy, 'http://wap.10086.cn/')
    #https_bool=validUsefulProxy(proxy, 'https://m.so.com/')
    https_bool= None
    print proxy, " http:" + str(http_bool), " https:" + str(https_bool)
    if (http_bool or https_bool):
        writ(proxy)

###########################################################

def writ(str):
    now=time.strftime('%Y%m%d',time.localtime(time.time()))
    try:
        fp = open("/sdcard/ip_"+now+".txt", "r")
        tmp=fp.read()
        fp = open("/sdcard/ip_"+now+".txt", "a")
        if(tmp.find(str)==-1):
            fp.write(str+"\r\n")
        fp.close()
    except:
        fp=open("/sdcard/ip_"+now+".txt", "a")
        fp.write(str+"\r\n")
        fp.close()

###########################################################
while (1):
    freeProxySecond(100)
