import urllib2

proxy = urllib2.ProxyHandler({'http':'117.172.98.71:8123'})
opener = urllib2.build_opener(proxy)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')

position = str.find(response.read(),'t3.baidu.com')
print position

