# __author__ = 'windmgc'
## The program is used for get proxy list from  http://mesk.cn ##
import os
import urllib2
import redis
import re
import time
# import threading
import random
from multiprocessing import Pool

## Connection of Redis Databases ##
RedisIO = redis.StrictRedis(host='localhost', port=6379, charset='utf-8', password='xidian123')

## Fetching Latest URL ##
def fetchLatestURL():
    getProxyUrl = 'http://www.mesk.cn/ip/china/'
    proxyUrlContent = urllib2.urlopen(getProxyUrl).read()
    linkReg = r"href=\"(.+?html)\""
    newUrl = re.findall(re.compile(linkReg),proxyUrlContent)[0]
    meskAddr = 'http://www.mesk.cn'
    newUrl = meskAddr + newUrl
    return newUrl

## Read HTML Contents ##
def getLatestProxy(newUrl):
    htmlContent = urllib2.urlopen(newUrl).read()
    print "Successfully Read HTML"

    ipsreg='<div>\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}:\d{1,5}@HTTP'
    rawips=re.findall(ipsreg,htmlContent)
    rawaddress=[]
    for i in rawips:
        rawaddress.append(i[5:-5])

    return rawaddress

def checkOneProxy(proxyAddress):
    testUrl = "http://www.baidu.com/"
    testString = "030173"
    testProxy = urllib2.ProxyHandler({'http':proxyAddress.split('\n')[0]})
    testOpener = urllib2.build_opener(testProxy)
    urllib2.install_opener(testOpener)
    t1=time.time()
    if(testUrl.find("?")==-1):
        testUrl=testUrl+'?rnd='+str(random.random())
    else:
        testUrl=testUrl+'&rnd='+str(random.random())
    try:
        f = urllib2.urlopen(testUrl,timeout=5)
        s = f.read()
        pos = s.find(testString)
    except:
        pos = -1
        pass
    t2=time.time()
    timeUsed=t2-t1
    if (timeUsed-5 < 0):
        return proxy
    else:
        return -1

if __name__ == '__main__':
    newUrl=fetchLatestURL()
    rawAddress = getLatestProxy(newUrl)
    pool = Pool()
    pool.map(checkOneProxy,rawAddress)
    pool.close()
    pool.join()
    for i in pool:
        print i
    #
    # for i in rawAddress:
    #     RedisIO.hset("proxy_pool",i,0)