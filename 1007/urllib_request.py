import urllib2

wq = urllib2.urlopen("http://www.baidu.com/")

html = wq.read()

print(html.decode(encoding="utf-8"))

f = open("test1.html","wb")

f.write(html)

f.close()

