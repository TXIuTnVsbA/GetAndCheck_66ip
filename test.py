#coding=utf8
import re
import requests
import thread
import sys
import time
requests.packages.urllib3.disable_warnings()
########################################################
def GetProxy(proxy_number=10):
    HEADER = {'Connection': 'keep-alive',
              'Cache-Control': 'max-age=0',
              'Upgrade-Insecure-Requests': '1',
              'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko)',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
              'Accept-Encoding': 'gzip, deflate, sdch',
              'Accept-Language': 'zh-CN,zh;q=0.8',
              }
    #url = "http://www.66ip.cn/mo.php?sxb=&tqsl={}&port=80".format(proxy_number)
    url="http://www.66ip.cn/mo.php?sxb=&tqsl={}&port=80&export=&ktip=&sxa=&submit=%CC%E1++%C8%A1&textarea=".format(proxy_number)
    html = requests.get(url, headers=HEADER).content
    for proxy in re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}', html):
        Online_CheckProxy_Custom(proxy)
########################################################
def Online_CheckProxy(ip,port):
    HEAD = {'Origin': 'http://www.66ip.cn',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://www.66ip.cn/yz/'}
    Post_data = 'ipadd='+ip+':'+str(port)
    print requests.post(url='http://www.66ip.cn/yz/post.php', headers=HEAD, data=Post_data).content
########################################################
def Online_CheckProxy_NotPort(ip):
    HEAD = {'Origin': 'http://www.66ip.cn',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://www.66ip.cn/yz/'}
    Post_data = 'ipadd='+ip
    print requests.post(url='http://www.66ip.cn/yz/post.php', headers=HEAD, data=Post_data).content
########################################################
def Online_CheckProxy_Custom(ip):
    HEAD = {'Origin': 'http://www.66ip.cn',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'http://www.66ip.cn/yz/'}
    Post_data = 'ipadd='+ip
    req = requests.post(url='http://www.66ip.cn/yz/post.php', headers=HEAD, data=Post_data).content
    print req
    if(req.find('能提供Http代理功能')!=-1):
        writ(req)
########################################################
def Offline_CheckProxy(proxy,url):
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
########################################################
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
if __name__ == '__main__':
	while (1):
		GetProxy(50)
