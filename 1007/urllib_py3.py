import urllib.request
ha = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"}
url = urllib.request.Request('http://www.baidu.com/',headers=ha)

#file=urllib.request.urlopen(url)

file=urllib.request.urlopen(url)
data=file.read()    #读取全部

#dataline=file.readline()    #读取一行内容

fhandle=open("test2.html","wb")    #将爬取的网页保存在本地
fhandle.write(data)
fhandle.close()

