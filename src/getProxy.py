# __author__ = 'windmgc'
## The program is used for get proxy list from  http://mesk.cn ##
import os
import urllib2
import redis
import re
import time
import random
from multiprocessing import Pool


## Connection of Redis Databases ##
RedisIO = redis.StrictRedis(host='localhost', port=6379, charset='utf-8', password='')


## Clean Proxy and Reset Counter##
def cleanUp():
    if RedisIO.exists("proxy_pool"):
        proxyPool=RedisIO.hkeys("proxy_pool")
        proxyPoolCounter=[]
        for i in proxyPool:
            counter = RedisIO.hget("proxy_pool",i)
            proxyPoolCounter.append(counter)
        for i in range(0,proxyPoolCounter.__len__()):
            if int(proxyPoolCounter[i]) >= 600:
                RedisIO.hdel("proxy_pool",proxyPool[i])
                print "del"+proxyPool[i]
        proxyPool=RedisIO.hkeys("proxy_pool")
        for i in proxyPool:
            RedisIO.hset("proxy_pool",i,"0")


## Fetching Latest URL ##
def fetchLatestURL():
    getProxyUrl = 'http://www.mesk.cn/ip/china/'
    proxyUrlContent = urllib2.urlopen(getProxyUrl).read()
    linkReg = r"href=\"(.+?html)\""
    newUrl = re.findall(re.compile(linkReg),proxyUrlContent)[0]
    meskAddr = 'http://www.mesk.cn'
    newUrl = meskAddr + newUrl
    print newUrl
    return newUrl


## Read HTML Contents ##
def getLatestProxy(newUrl):
    htmlContent = urllib2.urlopen(newUrl).read()
    print "Successfully Read HTML"
    filePointer = open("meskcn.html",'w')
    filePointer.write(htmlContent)
    ipsreg='\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,4}'
    rawips=re.findall(ipsreg,htmlContent)
    # rawaddress=[]
    # for i in rawips:
    #     rawaddress.append(i[5:-5])
    return rawips


def checkOneProxyExist(proxyAddress):
    if int(RedisIO.hexists("proxy_pool", proxyAddress)) == 0:
        RedisIO.hset("proxy_pool", proxyAddress, "0")


def main():
    cleanUp()
    newUrl = fetchLatestURL()
    rawAddress = getLatestProxy(newUrl)
    pool = Pool(20)
    pool.map(checkOneProxyExist,rawAddress)
    pool.close()
    pool.join()
    print 'Latest proxies have been imported into Redis hash table.'

if __name__ == '__main__':
    main()


