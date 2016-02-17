# __author__ = 'windmgc'
## The program will be running during 24 hours to check the proxy list. ##
import os
import urllib2
import redis
import time
import random
from multiprocessing import Pool

## Connection of Redis Databases ##
RedisIO = redis.StrictRedis(host='localhost', port=6379, charset='utf-8', password='')

## Check one proxy with Baidu.com ##
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
        f = urllib2.urlopen(testUrl,timeout=3)
        s = f.read()
        pos = s.find(testString)
    except:
        pos = -1
        pass
    t2=time.time()
    timeUsed=t2-t1
    if timeUsed-3 < 0 and pos != -1:
        pass
    else:
        RedisIO.hincrby("proxy_pool",proxyAddress)


if __name__ == '__main__':
    for i in range(20):
        proxyPool=RedisIO.hkeys("proxy_pool")
        pool = Pool(40)
        pool.map(checkOneProxy,proxyPool)
        pool.close()
        pool.join()
    # count=0
    # proxyPool=RedisIO.hkeys("proxy_pool")
    # for i in proxyPool:
    #     # print i
    #     if RedisIO.hget("proxy_pool",i) == '0':
    #         print i
    #         count = count + 1
    # print count