# __author__ = 'windmgc'
## The program will be running during 24 hours to check system status ##

import os
import urllib2
import redis
import time
import random
from multiprocessing import Pool

def reportProxyStatus():
    RedisIO = redis.StrictRedis(host='localhost', port=6379, charset='utf-8', password='')
    if RedisIO.exists("proxy_pool"):
        proxyList=RedisIO.hkeys("proxy_pool")
        if os.path.isfile(os.getenv("HOME")+"/proxyStatusLog.log"):
            filePointer=os.open(os.getenv("HOME")+"/proxyStatusLog.log")
            proxyListPrevious=filePointer.readlines()
            for i in proxyListPrevious:
                print i
    else:
        print "Proxy pool not exist."

# def reportClusterStatus():
#
# def reportGatewayStatus():
#
# def reportNetworkStatus():


def main():
    reportProxyStatus()

if __name__ == '__main__':
    main()