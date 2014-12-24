import urllib2
from sgmllib import SGMLParser

class ProxyIP (SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_td = ""
        self.name = []
    def start_td(self,attrs):
        self.is_td = 1
    def end_td(self):
        self.is_td = ""
    def handle_data(self, text):
        if self.is_td == 1:
            self.name.append(text)

content = urllib2.urlopen('http://pachong.org/').read()
proxies = ProxyIP()
proxies.feed(content)
for item in proxies.name:
    # print item.decode('gbk').encode('utf8')
    print item