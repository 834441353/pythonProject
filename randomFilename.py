import os
import random
from queue import Queue
import shutil

rootpath = "../NIR_ALL"
outpath = "../NIR_ALL1"


def rfirstdir():
    firstdirlsit = os.listdir(rootpath)
    random.shuffle(firstdirlsit)
    for i in firstdirlsit:
        pass


def rfilename(firstdirname, model):
    srcQ = Queue()
    dstQ = Queue()
    filenamelsit = os.listdir(os.path.join(rootpath, firstdirname, model))
    len_filenamelist = len(filenamelsit)
    # print(len_filenamelist)
    for i in range(len_filenamelist):
        srcQ.put(filenamelsit[i])
    random.shuffle(filenamelsit)
    for i in range(len_filenamelist):
        dstQ.put(filenamelsit[i])
    for i in range(len_filenamelist):
        a = str(srcQ.get())
        b = str(dstQ.get())
        srcfilename = rootpath+'/'+firstdirname + '/' + model + a
        # dstfilename = outpath + firstdirname + '/' + model + '/' + a
        print(srcfilename)
        # shutil.copyfile()
    print('end')


if __name__ == '__main__':
    rfilename('0000000003', 'Glass')
