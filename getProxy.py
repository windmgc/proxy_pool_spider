import urllib2
from sgmllib import SGMLParser

class getProxyList (SGMLParser):
    def __init__(self):
        SGMLParser.__init__(self)
        self.is_td = ""
        self.content = []
    def start_td(self,attrs):
        self.is_td = 1
    def end_td(self):
        self.is_td = ""
    def handle_data(self, text):
        if self.is_td == 1:
            self.content.append(text)

# class getTBODY (SGMLParser):
#     def __init__(self):
#         SGMLParser.__init__(self)
#         self.content = []
#         self.is_tbody = ""
#     def start_tbody(self,attrs):
#         self.is_tbody = 1
#     def end_tbody(self):
#         self.is_tbody = ""
#     def handle_data(self, text):
#         if self.is_tbody == 1:
#             self.content.append(text)

# class getANIMALS ():
#     def __init__(self):
#         self.rawData=""
#     def getanimals(self):


content = urllib2.urlopen('http://pachong.org/area/short/name/cn.html').read()

fp = open("test.txt",'w')
fp.write(content)
fp.close()

fp1 = open("test.txt",'r')
fpcontent=fp1.readlines()
# print fpcontent[12][31:-10]
animals=fpcontent[12][31:-10].split(';')
print animals
for i in animals:
    i=i[4:]
    print i
    exec(i)
fp1.close()

proxies = getProxyList()
proxies.feed(content)
# print proxies.content[9]
# print proxies.content[10]
# print proxies.content
# fp2 = open("test.txt",'w')
# for i in proxies.content:
#     print i
#     fp2.write(i)
# fp2.close()
