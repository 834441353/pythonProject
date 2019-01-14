
import time
for i in range(1,101):
    print("\r%.2f%%"%i, end='')
    time.sleep(0.01)

print("")

'''
try:
    fh = open("testfile", "x")
    fh.write("这是一个测试文件，用于测试异常!!")
except IOError:
    print("Error: 没有找到文件或读取文件失败")
    fh = open("testfile", "w")
    fh.write("这是一个测试文件，用于测试异常!222222222222!")
else:
    print("内容写入文件成功")
    fh.close()
'''
'''
from multiprocessing import Pool
from multiprocessing import cpu_count
import time

def work(num):
    print('num:%d'%num)
    time.sleep(1)

po = Pool(4)
for i in range(10):
    po.apply_async(work,(i+1,))
po.close()
po.join()
print(cpu_count())

'''
'''
import os

re1 =os.fork()

re2 = os.fork()
re3 = os.fork()
if re1 == 0:
    if re2 == 0:
        if re3 == 0:
            print('p1 %d'%os.getpid())
        else:
            print('p2 %d'%os.getpid())
    else:
        if re3 == 0:
            print('p3 %d'%os.getpid())
        else:
            print('p4 %d'%os.getpid())
else:
    if re2 == 0:
        if re3 == 0:
            print('p5 %d'%os.getpid())
        else:
            print('p6 %d'%os.getpid())
    else:
        if re3 == 0:
            print('p7 %d'%os.getpid())
        else:
            print('p8 %d'%os.getpid())
'''