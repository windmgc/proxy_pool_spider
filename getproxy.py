#!/usr/bin/python
#coding:utf-8

import urllib2,string
import time
import random
import re
import threading

proxy_array=[]

target_url="http://www.baidu.com/" #验证代理访问的地址
target_string="030173"
target_timeout=3                  #30s

#获取代理ip
def get_proxy():
    proxyurl = 'http://www.mesk.cn/ip/china/list_70_1.html'
    print proxyurl
    proxypage = urllib2.urlopen(proxyurl)
    proxyhtml = proxypage.read()
    linkreg = r"href=\"(.+?html)\""
    newlink = re.findall(re.compile(linkreg),proxyhtml)[0]
    print newlink
    url = 'http://www.mesk.cn'
    newurl = url+newlink
    print newurl
    newhtml = urllib2.urlopen(newurl).read()
    ipportreg = '\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}:\\d{1,5}'
    ipports = re.findall(re.compile(ipportreg),newhtml)
    for i in range(len(ipports)):
        check_one_proxy(ipports[i])

#验证代理ip
def check_one_proxy(ipport):
    global proxy_array
    global target_url,target_string,target_timeout
    ip = ipport.split(':')[0]
    port = ipport.split(':')[1]    
    url = target_url
    checkstr = target_string
    timeout = target_timeout
    proxies = {'http':ip+':'+port}
    proxy = urllib2.ProxyHandler(proxies)
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
    t1 = time.time()
    
    if(url.find("?")==-1):
        url=url+'?rnd='+str(random.random())  
    else:  
        url=url+'&rnd='+str(random.random())
    try:  
        f = urllib2.urlopen(url)  
        s= f.read()       
        pos=s.find(checkstr)  
    except:  
        pos=-1  
        pass  
    t2=time.time()
    
    timeused=t2-t1  
    with open('proxyip1.txt','a+') as f:
        if (timeused<timeout and pos>0):  
            print ipport
            f.writelines(ipport+'\n')

print 'start...'
get_proxy()
print 'end...'
