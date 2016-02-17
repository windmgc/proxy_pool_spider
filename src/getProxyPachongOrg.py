# __author__ = 'windmgc'
## The program is used for get proxy list from http://pachong.org ##

htmlContent = urllib2.urlopen('http://pachong.org/').read()
print "Successfully Read HTML"

fp = open("test.txt",'w')
fp.write(htmlContent)
fp.close()

fp1 = open("test.txt",'r')
fpcontent=fp1.readlines()
animals=fpcontent[12][31:-10].split(';')
for i in animals:
    i=i[4:]
    exec(i)
print "Successfully Read Animals"
fp1.close()

rawips=[]
ips=[]
ipsreg='<td>\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}\\.\\d{1,3}<\/td>'
rawips=re.findall(ipsreg,htmlContent)
for i in rawips:
    ips.append(i[4:-5])
print "Successfully Read IPs"

rawports=[]
ports=[]
portsreg='<td><script>\s*.*<\/script><\/td>'
rawports=re.findall(portsreg,htmlContent)
# counter=1
# for i in ports:
#     print i[26:-16]
#     print counter
#     counter+=1
for i in rawports:
    exec("ports.append("+i[26:-15]+")")
print "Successfully Read Ports"
# for i in ports2:
#     print i

fp2 = open("proxyListPachongOrg",'w')
i=0
while i<50:
    fp2.write(ips[i] + ":" + str(ports[i]) + "\n")
    i+=1



