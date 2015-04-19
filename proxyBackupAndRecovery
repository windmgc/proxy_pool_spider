#!/usr/bin/python
#coding:utf-8
#auth:cutoutsy
#function:back up the proxy

import redis
import sys

# Connection of Redis Databases
RedisIO_0 = redis.StrictRedis(host='localhost', port=6379, charset='utf-8',password='xidian123')
RedisIO_1 = redis.StrictRedis(host='localhost', port=6379, charset='utf-8',password='xidian123',db=1)

#backup the ip_port and errer numbers
def backupProxy():
	if RedisIO_0.exists('ip_port'):
		allproxy = RedisIO_0.hgetall('ip_port')
		for i in allproxy:
			ip_port = i
			error_num = RedisIO_0.hget('ip_port',ip_port)
			RedisIO_1.hset("ip_port_backup",ip_port,error_num)
	else:
		print 'the ip_port not exists in the redis'
#recovery the ip_port to redis
def recoveryProxy():
	if RedisIO_1.exists('ip_port_backup'):
		allproxy = RedisIO_1.hgetall('ip_port_backup')
		for i in allproxy:
			ip_port = i
			error_num = RedisIO_1.hget('ip_port_backup',ip_port)
			RedisIO_0.hset("ip_port",ip_port,error_num)
	else:
		print 'the ip_port_backup not exists in the redis'


if __name__ == '__main__':
    if sys.argv[1] == 'backup':
    	backupProxy()
    	print 'backup ok!'
    elif sys.argv[1] == 'recovery':
    	recoveryProxy()
    	print 'recovery ok!'
    else:
    	print 'the argv wrong!'
	