import urllib2
import time
import random

target_url="http://www.baidu.com/" #验证代理访问的地址
target_string="030173"
target_timeout=3                  #30s

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
